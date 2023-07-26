from sqlmodel import Field, Session, create_engine


SQLALCHEMY_DATABASE_URL = "sqlite:///./db.sqlite3"




engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

SessionLocal = Session(engine)

