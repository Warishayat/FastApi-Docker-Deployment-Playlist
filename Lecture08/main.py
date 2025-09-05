from Routers import UserAuthentication
from fastapi import FastAPI,Depends
from Config.database import engine,get_db
from Schemas import UserCredential
from sqlalchemy.orm import Session

app = FastAPI()

UserCredential.Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return{
        "message" : "Hello world"
    }

#Make database route to check everything is working fine in both schemas
@app.get("/checkDatabase")
def checkDatabase(db:Session=Depends(get_db)):
    return{
        'success' : True,
        "Message" : "Database is up"
    }

# Authentication Routes
app.include_router(UserAuthentication.router)