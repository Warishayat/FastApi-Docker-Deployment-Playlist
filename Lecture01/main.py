from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI(
    title="CopyMate-AI Powerd Backend Api's",
    description="A collection of APIs for full-stack development, allowing you to experiment, test, and connect seamlessly with your frontend projects",
    version='0.1.0',
)


#Get  request
@app.get('/')  
async def welcome():
    return {"message": "hello world"}

@app.get("/get_user")
async def getuser():
    return{
        "message" :  "Ai is getting the memeber of your group wait for the moment"
    }

#post request
@app.post('/create_post')
async def creatPost():
    return { 
        "message"  : "Your post has been created Successfully."
    }

#post request with body
@app.post('/create_user')
async def creatPost(payload: dict = Body(...)):
    return { 
        "title" : f"The Title is {payload['Title']}",
        "description"  : f"The description is {payload['description']}",
        "message" : "This post has successfully created in the datababase"
    }
