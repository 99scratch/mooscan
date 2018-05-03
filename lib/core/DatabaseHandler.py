import os
import sqlalchemy
from sqlalchemy.orm import sessionmaker
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
            self.sess = sessionmaker(bind=engine)
        except:
            self.create_database(engine)

        if (not engine.dialect.has_table(engine, Modules.__tablename__)) and \
            (not engine.dialect.has_table(engine, Code.__tablename__)):
                self.create_database(engine)

    def save_module(self, module):

        nameparts = module['frankenstyle'].split('_')
        shortname = nameparts[1]

        session = self.sess()

        thismodule = session.query(Modules).filter_by(name_frankenstyle=module['frankenstyle']).first()

        if module is None:
            thismodule = Modules(
                 type=module['plugintype']['type'],
                 name=module['name'],
                 shortname=shortname,
                 name_frankenstyle=module['frankenstyle'],
                 desc=module['shortdescription'],
                 lastrelease=module['timelastreleased']['iso8601date'],
                 url=module['url']
                 )

            session.add(thismodule)
        else:
            thismodule.type = module['plugintype']['type']
            thismodule.name = module['name']
            thismodule.shortname = shortname
            thismodule.desc = module['shortdescription']
            thismodule.lastrelease = module['timelastreleased']['iso8601date']
            thismodule.url = module['url']

        session.commit()

