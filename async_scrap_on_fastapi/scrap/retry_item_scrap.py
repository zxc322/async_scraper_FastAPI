import os, sys
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)  
sys.path.append(parent_directory)

import asyncio
from rabbit.data_item_consumer import RabbitDataConsumer
from scrap.web.retry_scrap import RetryScrape

            
retry = RetryScrape()
chunk = list()

async def async_pull_all(base_urls):
    return await asyncio.gather(*[retry.item_scraper.get_item(url) for url in base_urls])


def callback(ch, method, properties, url):
    url = url.decode("utf-8")
    chunk.append(url)
    print(f'--- urls loaded {len(chunk)} --- (press CTRL+C to parse loaded urls) ---')



if __name__ == "__main__":
    try:
        RabbitDataConsumer().bad_items_consume(callback=callback)
    except KeyboardInterrupt:
        print('Interrupted')

retry.send_to_parse(chunk=chunk, func=async_pull_all)