import sys, os
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)  
sys.path.append(parent_directory)

import pika

from constants.config import RABBITMQ_DEFAULT_USER, RABBITMQ_DEFAULT_PASS


credentials = pika.PlainCredentials(RABBITMQ_DEFAULT_USER, RABBITMQ_DEFAULT_PASS)

parameters = pika.ConnectionParameters(
    'rabbitmq-host', 
    5672, '/', 
    credentials=credentials, 
    heartbeat=60*20
    )

