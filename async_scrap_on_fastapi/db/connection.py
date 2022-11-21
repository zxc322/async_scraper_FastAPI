import sys, os
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)  
sys.path.append(parent_directory)

from sqlalchemy.ext.declarative import declarative_base
import databases
from constants.config import DATABASE_URL


database = databases.Database(DATABASE_URL)
Base = declarative_base()

async def db_connect():
    await database.connect()
    return database