from Config.database import base
from sqlalchemy import Column,Integer,String,Boolean
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text

class UserData(base):
    
    __tablename__ = "Users"

    id =  Column(Integer,primary_key=True,nullable=True)
    name = Column(String,nullable=True)
    email = Column(String,nullable=True)
    password = Column(String,nullable=True)
    created_At = Column(TIMESTAMP(timezone=True),nullable=True,server_default=(text("now()")))

