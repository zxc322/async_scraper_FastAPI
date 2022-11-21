import sys, os
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)  
sys.path.append(parent_directory)

import pika

from rabbit.connection import parameters


class RabbitLinksConsumer:

    def __init__(self) -> None:
        self.connection = pika.BlockingConnection(parameters)
        

    def consume(self, callback):
        chanel = self.connection.channel()
        chanel.queue_declare('items_urls', durable=True)
        chanel.basic_consume(
            queue='items_urls', on_message_callback=callback, auto_ack=True)
        print(' [*] Waiting for messages. To exit press CTRL+C')
        try:
            chanel.start_consuming()
        except:
            chanel.close()


    #  Pages with bad response were sended to this queue    
    def bad_links_consume(self, callback):
        chanel = self.connection.channel()
        chanel.queue_declare('bad_pages', durable=True)
        chanel.basic_consume(
            queue='bad_pages', on_message_callback=callback, auto_ack=True)
        print(' [*] Waiting for messages. To exit press CTRL+C')
        try:
            chanel.start_consuming()
        except:
            chanel.close()


