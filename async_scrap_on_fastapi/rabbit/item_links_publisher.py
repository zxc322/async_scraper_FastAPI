import sys, os
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)  
sys.path.append(parent_directory)

import pika
from rabbit.connection import parameters


class RabbitLinksPublisher:

    def __init__(self) -> None:
        self.connection = pika.BlockingConnection(parameters)
        
        

    def send_good_response(self, body):
        chanel = self.connection.channel()         
        chanel.queue_declare('items_urls', durable=True)     
        chanel.basic_publish(exchange='',
                    routing_key='items_urls',
                    body=body)


    def send_bad_response(self, body):  
        chanel = self.connection.channel()  
        chanel.queue_declare('bad_pages', durable=True)     
        chanel.basic_publish(exchange='',
                    routing_key='bad_pages',
                    body=body)