from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

database_url = os.getenv("database_url")
engine = create_engine(database_url)
sesssionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
base = declarative_base()


#to get the session of database
def get_db():
    db = sesssionLocal()
    try:
        yield db
    finally:
        db.close()
