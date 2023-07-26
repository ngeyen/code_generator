from sqlmodel import Session, create_engine


import os
from sqlmodel import create_engine, SQLModel, Session


# DATABASE_URL = os.environ.get("DATABASE_URL")
SQLALCHEMY_DATABASE_URL = "sqlite:///./db.sqlite3"
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True, connect_args={'check_same_thread': False}) 


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session