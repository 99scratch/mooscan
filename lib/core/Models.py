from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey


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


class Tags(Create.Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    tag = Column(String, unique=True)


class Files(Create.Base):
    __tablename__ = 'files'

    id = Column(Integer, primary_key=True)
    tag = Column(Integer,
                 ForeignKey("tags.id"),
                 nullable=False,
                 index=True)
    filepath = Column(String, index=True)
    filehash = Column(String, index=True)

class Versions(Create.Base):
    __tablename__ = 'versions'

    id = Column(Integer, primary_key=True)
    tag = Column(Integer,
                 ForeignKey("tags.id"),
                 nullable=False,
                 index=True)
    filepath = Column(String, index=True)
    version = Column(Integer, index=True)
    comment = Column(String)
    filehash = Column(String, index=True)

