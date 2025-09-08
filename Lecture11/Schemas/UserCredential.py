from sqlalchemy import Column,Integer,String,Boolean,ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from Config.database import Base

class UserCredentialsData(Base):
    __tablename__ = "UserCredentials"
    id =  Column(Integer,primary_key=True,nullable=False)
    name = Column(String,nullable=True)
    email = Column(String,nullable=True)
    password = Column(String,nullable=True)
    created_At = Column(TIMESTAMP(timezone=True),nullable=True,server_default=(text("now()")))

class Posts(Base):
    __tablename__ = "Posts"

    id =  Column(Integer,primary_key=True,nullable=False)
    # this is foreign key which will make realtion with the Usercredential table.
    user_id = Column(Integer,ForeignKey("UserCredentials.id",ondelete='CASCADE'),nullable=False)
    title = Column(String,nullable=True)
    content = Column(String,nullable=True)
    published = Column(Boolean,nullable=True,server_default=(text("false")))
    created_At = Column(TIMESTAMP(timezone=True),nullable=True,server_default=(text("now()")))
