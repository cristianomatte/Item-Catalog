from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("sqlite:///item-catalog.db")
Base = declarative_base()
db_session = scoped_session(sessionmaker(bind=engine))


def create_database():
    Base.metadata.create_all(engine)
