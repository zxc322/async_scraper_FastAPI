import sys, os
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)  
sys.path.append(parent_directory)

import pika
from rabbit.connection import parameters


class RabbitDataPublisher:

    def __init__(self) -> None:
        self.connection = pika.BlockingConnection(parameters)
        
        

    def send_good_response(self, body):
        chanel = self.connection.channel()          
        chanel.queue_declare('item_data', durable=True)     
        chanel.basic_publish(exchange='',
                    routing_key='item_data',
                    body=body)


    def send_bad_response(self, body):  
        chanel = self.connection.channel()
        chanel.queue_declare('bad_item_page', durable=True)     
        chanel.basic_publish(exchange='',
                    routing_key='bad_item_page',
                    body=body)