import os
import sqlalchemy
import time
import json
from sqlalchemy.orm import sessionmaker
from lib.core.TextHandler import TextHandler
from lib.core.Models import Create
from lib.core.Models import Code
from lib.core.Models import Modules
from lib.core.Models import DataUpdates
from lib.core.Models import Tags
from lib.core.Models import Versions
from lib.core.Models import Files


class DatabaseHandler(object):

    def __init__(self, arguments, config):
        self.arguments = arguments
        self.config = config

    def create_database(self, engine):
        TextHandler().debug("Creating Database")

        Create.Base.metadata.create_all(engine)

    def connect(self):
        TextHandler().debug("Connecting to the database")

        db_path = "sqlite:///{path}/{db}".format(
                path=self.config['path'],
                db=self.config['database']
                )

        TextHandler().debug("Database Path: {path}".format(path=db_path))
        engine = sqlalchemy.create_engine(db_path)
        try:
            self.conn = engine.connect()
            self.sess = sessionmaker(bind=engine)
        except:
            self.create_database(engine)

        if (not engine.dialect.has_table(engine, Modules.__tablename__)) and \
           (not engine.dialect.has_table(engine, Code.__tablename__)) and \
           (not engine.dialect.has_table(engine, DataUpdates.__tablename__)):
                self.create_database(engine)

    def get_updates(self):
        session = self.sess()
        updates = session.query(DataUpdates).first()
        if updates is None:
            return {}
        else:
            return updates

    def save_tag(self, thistag):
        session = self.sess()

        tag = session.query(Tags).filter_by(
                tag = thistag
                ).first()

        if tag is None:
            tag = Tags(tag=thistag)
            session.add(tag)

        session.commit()
        return tag.id

    def save_file_version(self, fileinfo):
        session = self.sess()

        ver = session.query(Versions).filter_by(
            tag = fileinfo['tag'],
            filepath = fileinfo['path'],
            version = fileinfo['version'],
            comment = fileinfo['comment'],
            filehash = fileinfo['hash']).first()

        if ver is None:
            ver = Versions(
                    tag = fileinfo['tag'],
                    filepath = fileinfo['path'],
                    version = fileinfo['version'],
                    comment = fileinfo['comment'],
                    filehash = fileinfo['hash'])

            session.add(ver)

        session.commit()

    def save_updates(self, update):
        session = self.sess()
        # Save the update data here
        lastupdate = session.query(DataUpdates).first()

        if lastupdate is None:
            lastupdates = {}
        else:
            lastupdates = json.loads(lastupdate.updates)

        if update == 'modules':
            lastupdates['modules'] = int(time.time())
        elif update == 'code':
            lastupdates['code'] = int(time.time())

        if lastupdate is None:
            data = json.dumps(lastupdates)
            thisupdate = DataUpdates(updates=data)
            session.add(thisupdate)
        else:
            lastupdate.updates = json.dumps(lastupdates)

        session.commit()

    def save_module(self, module):

        nameparts = module['frankenstyle'].split('_')
        shortname = nameparts[1]

        session = self.sess()

        thismodule = session.query(Modules).filter_by(
                name_frankenstyle=module['frankenstyle']
                ).first()

        if thismodule is None:
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
