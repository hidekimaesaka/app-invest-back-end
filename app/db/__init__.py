from os import getenv

from sqlalchemy import create_engine

from sqlalchemy.orm import Session, DeclarativeBase

class Base(DeclarativeBase):
    pass


db_uri = getenv('DB_URI')
engine = create_engine(db_uri, echo=True)
session = Session(engine)
