import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)  
sys.path.append(parent_directory)

from databases import Database
from db.models import users_table, items_table, overviews_table, units_table


class GenericInit:

    def __init__(self, db: Database):
        self.users = users_table
        self.items = items_table
        self.overview = overviews_table
        self.units = units_table
        self.db = db