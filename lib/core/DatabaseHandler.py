import os
import sqlalchemy
from lib.core.TextHandler import TextHandler
from lib.core.Models import Create
from lib.core.Models import Code
from lib.core.Models import Modules


class DatabaseHandler(object):

    def __init__(self, arguments, config):
        self.arguments = arguments
        self.config = config

    def create_database(self, engine):
        TextHandler().debug("Creating Database")

        Create.Base.metadata.create_all(engine)

    def connect(self):
        TextHandler().debug("Connecting to the database")

        db_path = "sqlite:///{path}/{db}".format(path=self.config['path'], db=self.config['database'])
        TextHandler().debug("Database Path: {path}".format(path=db_path))
        engine = sqlalchemy.create_engine(db_path)
        try:
            self.conn = engine.connect()
        except:
            self.create_database(engine)

        if (not engine.dialect.has_table(engine, Modules.__tablename__)) and \
            (not engine.dialect.has_table(engine, Code.__tablename__)):
            self.create_database(engine)
