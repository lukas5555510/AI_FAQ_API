from sqlalchemy.orm import DeclarativeBase
from src.app.session import engine


class Base(DeclarativeBase):
    pass


def init_db():
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully")