from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


class Create():

    Base = declarative_base()

class Modules(Create.Base):
    __tablename__ = 'modules'

    id = Column(Integer, primary_key=True)
    type = Column(String)
    name = Column(String)
    name_frankenstyle = Column(String)
    desc = Column(String)
    lastrelease = Column(String)
    url = Column(String)

class Code(Create.Base):
    __tablename__ = 'code'

    id = Column(Integer, primary_key=True)
