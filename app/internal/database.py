from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from .schema import Base, Beer, BeerData

DATABASE_URI = 'postgresql+psycopg2://postgres:12345678@localhost/api'


engine = create_engine(DATABASE_URI)
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
