import os, sys
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)  
sys.path.append(parent_directory)

import asyncio
import time

from constants.web_data import LOCATIONS
from scrap.web.scrap_links import LinkScraper


async def async_pull_all(base_urls):
    return await asyncio.gather(*[scraper.get_urls(url) for url in base_urls])


def chose_region():
    print('Chose location as single number...')
    for k, v in LOCATIONS.items():
        print(f'{k} => {v}')

    while True:
        province_id = input('Number (0<n<11): ')
        if province_id == 'all':
            return [LOCATIONS[x] for x in range(1, 11)]
        elif province_id.isnumeric() and (int(province_id) > 0 and int(province_id) < 11):
            return LOCATIONS.get(int(province_id))
    

def pages_to_parse(province: tuple):
    for i in range(21, 102, 20):
                start = i-20
                end=i
                print(start, '--', end)

                base_urls = ('https://www.kijiji.ca/{}/page-{}/{}?siteLocale=en_CA'.format(
                    province[0], page, province[1]) for page in range(start, end))
            
                asyncio.run(async_pull_all(base_urls=base_urls))
                print(f'--- Found {scraper.total_urls} urls ---') 
                print(f' --- good request:  {scraper.good_pages} pages , bad response: {scraper.bad_pages} ---')
                print('sleeping 10...')
                time.sleep(10)



if __name__ == "__main__":
    scraper = LinkScraper()
    start_time = time.time()
    province = chose_region()

    if isinstance(province, list):
        for reg in province:
            pages_to_parse(province=reg)
    else:
        pages_to_parse(province=province)
    print(f'--- finished {time.time()-start_time}. Found {scraper.total_urls} urls ---')

        



    

