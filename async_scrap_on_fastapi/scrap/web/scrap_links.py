import os, sys
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)  
sys.path.append(parent_directory)

import httpx
from bs4 import BeautifulSoup as BS

from constants.web_data import headers
from rabbit.item_links_publisher import RabbitLinksPublisher


class LinkScraper():

    def __init__(self):
        self.rabbit = RabbitLinksPublisher()
        self.urls = list()
        self.total_urls = 0
        self.good_pages = 0
        self.bad_pages = 0


    async def get_urls(self, url):
        async with httpx.AsyncClient(timeout=None) as client:
            
            url = url.replace('page-1/', '') if 'page-1/' in url else url

            response = await client.get(url=url, headers=headers)            
            
            print(f'[DEBUG] status {response.status_code}\n')
            print(f'[DEBUG] headers {response.headers}\n')
            print(f'[DEBUG] req.headers {response.request.headers}\n')
            print(f'[DEBUG] cookies {response.cookies}\n\n')
            
            print(f'--- status {response.status_code} ---')
            if response.status_code == 302:
                url = response.headers['location']
                url = 'https://www.kijiji.ca' + url
                print(f'--- 302 {url}\n ---REDIRECTING---')
                response = await client.get(url=url, headers=headers) 



            soup = BS(response.text, 'lxml')
            containers = soup.find_all('div', class_='info-container')
            print(f'--- found {len(containers)} urls on page {response.url} ---')
            

            if len(containers) == 0:
                self.bad_pages += 1
                self.rabbit.send_bad_response(str(response.url))
            else:
                self.good_pages += 1
                for el in containers:
                    url = el.find('div', class_='title').a.get('href')
                    url = 'https://www.kijiji.ca' + url
                    self.total_urls += 1
                    print(f'sending {url}')
                    self.rabbit.send_good_response(url)