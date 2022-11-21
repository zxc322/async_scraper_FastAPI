import sys, os
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)  
sys.path.append(parent_directory)
import json

from scrap.bs4.item_parse_methods import BS4Parse
from scrap.bs4.complete_item_dict import CompleteDict
from rabbit.data_item_publisher import RabbitDataPublisher



class ItemParser():

    def __init__(self):
        self.item_counter = 0

         

    async def item_data(self, html, item_url):
        parser =  BS4Parse(html=html, item_url=item_url)
        if not await parser.health_check():
            print('send bad response', item_url)
            RabbitDataPublisher().send_bad_response(body=item_url)
        else:
            complete_dict = CompleteDict(parser)   
            self.item_counter += 1
            user_dict = await complete_dict.user_insert()
            item_dict = await complete_dict.item_insert()
            overview_dict = await complete_dict.overview_dict()
            units_dict = await complete_dict.unit_dict()
            data = [user_dict, item_dict, overview_dict, units_dict]
            print(data, sep='\n')
            print(f'\n--- DONE ---       --- item - {self.item_counter} ---\n')

            to_rabbit = json.dumps(data)
            RabbitDataPublisher().send_good_response(body=to_rabbit)

            
    
        