import os, sys
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)  
sys.path.append(parent_directory)

import asyncio
import time

from rabbit.item_links_consumer import RabbitLinksConsumer
from scrap.web.scrap_items import ItemScraper          

scraper = ItemScraper()

async def async_parse_items(urls):
    return await asyncio.gather(*[scraper.get_item(url) for url in urls])

def callback(ch, method, properties, url):
    url = url.decode("utf-8")
    if url == 'force':
        print(f'runing urls {scraper.urls}')
        asyncio.run(async_parse_items(scraper.urls))
        scraper.urls = list()
       
    else:    
        print('^__^')
        url += '?siteLocale=en_CA' # To prevent French pages 
        scraper.urls.append(url)
        if len(scraper.urls) > 15:
            print(f'runing urls {scraper.urls}')
            asyncio.run(async_parse_items(scraper.urls))
            print('sleeping 15 ...')
            time.sleep(15)
            scraper.urls = list()




if __name__ == "__main__":
    try:

        RabbitLinksConsumer().consume(callback=callback)
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
    


    

