from fastapi import FastAPI,Depends
from fastapi.exceptions import HTTPException
from Models import User
from Models.User import UserData
from Config.database import base,sesssionLocal,get_db,engine
from sqlalchemy.orm import Session
from Schemas.Schmas import ModelResponse
from typing import List


User.base.metadata.create_all(bind=engine)


app = FastAPI(
    title="AI Powerd Application of Machine Learning.",
    description="This is all about the machine learning and fastapi routes",
    version="1.2.3"
)


# What is diffrence between pydantic and schemas of database
# 1: What is pydantic ?
# Ans: pYDANTIC Model define the shape of request & response.
# Mean when user creating the post it define how the payload will look like.  

# 2: What is Schema Model?
# ANS: iTS REsponsible for defining the columns in database mean what colums should be there.
# it basically to use the queries with database like create update delete and retrive
# its basically diffrent from the pydantic we can skip the pydatic if we want,
# but we cant skip the schema models.pydantic just sure how the data should look like and what data we are expecting
 

@app.get("/")
def root():
    return{
        "success" : True,
        "message" : "Are you looking for Pong."
    }


@app.get("/testdb")
def getdatabase(db:Session=Depends(get_db)):
    return{
        "success" : True,
        "message" : "Till now everything is fine"
    }


@app.get("/alluser",response_model=List[ModelResponse])
def getalluser(db:Session=Depends(get_db)):
    alluser = db.query(UserData).all()
    if alluser:
        return alluser
    return HTTPException(
        status_code=404,
        detail="User not Found"
    )


@app.get("/singleuser",response_model=List[ModelResponse])
def singleUser(id:int,db:Session=Depends(get_db)):
    user = db.query(UserData).filter_by(id=id).first()
    if user:
        return{
            "success" : True,
                "User" : user
        }
    return  HTTPException(
        status_code=404,
        detail="User not Found"
    )
