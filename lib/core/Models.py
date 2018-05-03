from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


class Create():

    Base = declarative_base()


class DataUpdates(Create.Base):
    __tablename__ = 'dataupdates'

    id = Column(Integer, primary_key=True)
    updates = Column(String)


class Modules(Create.Base):
    __tablename__ = 'modules'

    id = Column(Integer, primary_key=True)
    type = Column(String, index=True)
    name = Column(String, index=True)
    shortname = Column(String, index=True)
    name_frankenstyle = Column(String, unique=True)
    desc = Column(String)
    lastrelease = Column(String)
    url = Column(String)


class Code(Create.Base):
    __tablename__ = 'code'

    id = Column(Integer, primary_key=True)
