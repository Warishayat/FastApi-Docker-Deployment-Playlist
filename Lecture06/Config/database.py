#Step1: Create the creat_engine ,make sessionlocal and Base

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQL_ALCHEMY_DATABASE_URL = 'postgresql://postgres:waris4200@localhost/fastapi'


def get_db():
    db = sessionLocal()
    try: 
        yield db
    finally:
        db.close()


engine = create_engine(SQL_ALCHEMY_DATABASE_URL)

sessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()