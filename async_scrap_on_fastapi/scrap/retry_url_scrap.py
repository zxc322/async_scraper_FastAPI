import os, sys
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)  
sys.path.append(parent_directory)

import asyncio
import time
from rabbit.item_links_consumer import RabbitLinksConsumer
from scrap.web.retry_scrap import RetryScrape

            
retry = RetryScrape()
chunk = list()

async def async_pull_all(base_urls):
    return await asyncio.gather(*[retry.link_scraper.get_urls(url) for url in base_urls])


def callback(ch, method, properties, url):
    url = url.decode("utf-8")
    chunk.append(url)
    print(f'--- urls loaded {len(chunk)} --- (press CTRL+C to parse loaded urls) ---')



if __name__ == "__main__":
    try:
        RabbitLinksConsumer().bad_links_consume(callback=callback)
    except KeyboardInterrupt:
        print('Interrupted')
        
retry.send_to_parse(chunk=chunk, func=async_pull_all)


    

