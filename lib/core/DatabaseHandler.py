import sqlite3
import os
from lib.core.TextHandler import TextHandler


class DatabaseHandler(object):

    def __init__(self, arguments, config):
        self.arguments = arguments
        self.config = config

    def create_databases(self):
        print("check for databases and create if needed")

    def create_code_db(self):
        if os.environ.get('MOOSCAN_DATA_PATH'):
            basepath = os.environ.get('MOOSCAN_DATA_PATH')
        else:
            basepath = self.config['mooscan_path']

        code_db_path = basepath + "/" + self.config['code_database']

        if not os.path.isfile(code_db_path):
            # Create the SQLite database
            TextHandler().info("Code version database was not found. "
                               "Creating...")
