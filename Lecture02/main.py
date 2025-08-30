# why we need schema becuase client sent the data whatever they  want.
# the data is not getting validate
# lets make a validate class like backend will tell the frntend i would like the accept the data lookm like.
# Bound User the data should be look like this

from fastapi import FastAPI
from fastapi.params import Body
from Models.Schema import ValidatePOst

app = FastAPI(
    title="AI - Powerd Application API'S",
    description=  " Test it with your Frontend Integration",
    version="0.1.1"
)


@app.get('/')
async def hello():
    return {
        'message' : "app is up"
    }

@app.post('/create_post')
async def createpost(payload:ValidatePOst):
    
    return{
       "message" : payload.dict()
    }