import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)  
sys.path.append(parent_directory)

import json

from repositories.create import Insert
from rabbit.data_item_consumer import RabbitDataConsumer
from db.connection import db_connect
from repositories.services.tools import sync


class InsertData:

    async def insert_data(self, data: list):
        crud = Insert(db=await db_connect())
        user_data, item_data, overview_data, units_data = data
        item = await crud.get_or_create_item(item_data=item_data, user_data=user_data)
        if not item.created_before:
            await crud.create_overview(item_id=item.id, overview_dict=overview_data)
            await crud.create_units(item_id=item.id, units_dict=units_data)

insert = InsertData()

counter = 0

@sync
async def callback(ch, method, properties, item):
    counter += 1
    print(f'[LOG] -- got new item # {counter} --')
    await insert.insert_data(data=json.loads(item))

if __name__ == '__main__':
    try:
        RabbitDataConsumer().consume(callback=callback)

    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)