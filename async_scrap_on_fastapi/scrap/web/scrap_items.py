import os, sys
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)  
sys.path.append(parent_directory)

import httpx

from constants.web_data import headers
from scrap.bs4.single_item_parse import ItemParser


class ItemScraper():

    def __init__(self) -> None:
        self.urls = list()
        self.parser = ItemParser()

    async def get_item(self, url: str):
        async with httpx.AsyncClient(timeout=None) as client:
            
            response = await client.get(url=url, headers=headers)

            print(f'[DEBUG] status {response.status_code}\n')
            print(f'[DEBUG] headers {response.headers}\n')
            print(f'[DEBUG] req.headers {response.request.headers}\n')
            print(f'[DEBUG] cookies {response.cookies}\n\n')


            if response.status_code == 302:
                url = response.headers['location']
                url = 'https://www.kijiji.ca' + url
                print(f'--- 302 {url}\n ---REDIRECTING---')
                response = await client.get(url=url, headers=headers)

            await self.parser.item_data(html=response.text, item_url=url)