import os, sys
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)  
sys.path.append(parent_directory)

import asyncio
import time
from scrap.web.scrap_links import LinkScraper
from scrap.web.scrap_items import ItemScraper

            
class RetryScrape:

    def __init__(self) -> None:
        self.link_scraper = LinkScraper()
        self.item_scraper = ItemScraper()


    def send_to_parse(self, chunk: list, func):
        while chunk:
            try:
                to_parse = chunk[:10]
                chunk = chunk[10:]
                asyncio.run(func(to_parse))
                print(f'retrying urls || urls left {len(chunk)}')
                print('sleeping 10 ...')
                time.sleep(10)
            except Exception as ex:
                print(f'parsing stopped : {ex}')
                break


