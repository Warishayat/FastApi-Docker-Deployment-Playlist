# in this class we wll discuss the ORM ==> NO MORE SQL object relational model
# No we will dicuss to thw orm and orm will dicuss to sql.
# orm provide us the flexibility of this.
# it works as translator for us in betwwen bakend and database.



# Step that we will follow in this lecture

## Step 1: instead of creating the dataasbe directly into the pgadmin
## We will create the database in the python and and we will define the filed there.
## Queries can be made through python code No sql is necessary.
## there are multiple orm but we will use sqlalchemy.Its not part of fastapi.


# Lets work with sql alchemy and make database

from fastapi import FastAPI,Depends
from fastapi.exceptions import HTTPException
from Schemas import UserSchema
from Schemas.UserSchema import Post
from Config.database import engine,get_db
from sqlalchemy.orm import Session
from Middleware.Datavalidation import ValidateUser,UpdateUserValidation


UserSchema.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Powerd Application",
    description = "This is ai powerd application with fastapi apis",
    version = "1.2.2"
)



@app.get("/")
def get_root():
    return{
        "message" : "Hello world"
    }



@app.get("/sqlalchemy")
def testpost(db:Session = Depends(get_db)):
    return {
        "status" : "success",
        "database" : "Database is up"
    }


@app.get("/allposts")
def getposts(db:Session=Depends(get_db)):
    posts=db.query(Post).all()
    if posts:
        return{
            "success" : True,
            "data" : posts
        }
    return HTTPException(
        status_code=404,
        detail= "User not found at this location"
    )


@app.get("/singlepost/{id}")
def getSinglePost(id:int ,db:Session=Depends(get_db)):
    singlepost = db.query(Post).filter_by(id=id).first()
    if singlepost:
        return{
            "success" : True,
            "Data" : singlepost
        }
    return HTTPException(
        status_code=404,
        detail=f"User not found crospond to this: {id}"
    )


#create a new user
@app.post("/creatnewUser")
def NewUser(payload: ValidateUser, db: Session = Depends(get_db)):
    try:
        new_user = Post(
            title=payload.title,
            content=payload.content,
            published=payload.published
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return {
            "success": True,
            "message": "User has been created successfully.",
            "user_id": new_user.id
        }
    except Exception as e:
        db.rollback()  
        raise HTTPException(
            status_code=500,
            detail=f"User could not be created. Error: {str(e)}"
        )
    
#update the user
@app.put('/updateUser/{id}')
def updateUser(id:int,payload:UpdateUserValidation,db:Session=Depends(get_db)):
    existPost = db.query(Post).filter_by(id=id).first()
    if not existPost:
        raise HTTPException(status_code=404,detail="User is not found in the database.")
    
    if payload.title is not None:
        existPost.title = payload.title
    if payload.content is not None:
        existPost.content = payload.content
    if payload.published is not None:
        existPost.published = payload.published

    try:
        db.commit()
        db.refresh(existPost)
        return {
            "success" : True,
            "message" : "User has been updated Successfully",
            "post": {
                "id": existPost.id,
                "title": existPost.title,
                "content": existPost.content,
                "published": existPost.published
            }
        }
    except Exception as e:
        raise HTTPException(
            status_code=404,
            detail="Something went wrong try agian later."
        )
        
#lets last delet the user
@app.delete("/deleteuser/{id}")
def deletuser(id:int,db:Session=Depends(get_db)):
    finduser = db.query(Post).filter_by(id=id).first()
    if finduser is None:
        raise HTTPException(status_code=404,detail="User not found.")
    try:
        db.delete(finduser)
        db.commit()
        return{
            "success" : True,
            "message" : "User is deleted Successfully from the database."
        }

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=e
        )