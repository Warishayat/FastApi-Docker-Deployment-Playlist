from fastapi import FastAPI,Path,Query
import json
from fastapi.exceptions import HTTPException

app = FastAPI()

# Path and Query Parameter.

# helper function  
def load_data():
    with open("patient.json","r") as file:
        data = json.load(file)
    return data

@app.get("/")
async def home():
    return {
        "message": "welcome to home page"
    }

@app.get("/view")
async def viewallpatient():
    data = load_data()
    return data


# get the specific patient from the data. aprams and dynamic segment will come in to the endpoint
#example i want to view only patient no 3 data
#Dynamic path
@app.get('/view/{id}')
async def viewSpecificPatient(id:int=Path(...,description="id of the patient in the database",example="1")):
    data = load_data()
    for patient in data:
        if patient["id"] == id:
            return{
                "message": "data is found",
                "data" : patient
            }
    raise HTTPException(status_code=404, detail="Patient not found")


# Http status code are 3 digit num return by the web server.
# 2** -> 20o mean successfull
# 3** -> further action need to take reedirect
# 4** -> There is sonme error on client side.
# 5** -> There is some error on server side.

#Famous status code in request
# 200 -> request is fullfill
# 201 reseource that you want to creat getting successful
# 204 successfull but void
# 400 bad request
# 401 unauthorized
# 404 not found
# 500 server error
# 502 communciation broken



#Query parameter
# @app.get('/sort')
# async def sortpatient(sort_by:str=Query(...,description="sort on patient on the basis of their age",example="low age will come first"), order:str=Query('asc',description="sor in asc order")):
#     valid_field = ["age"]
#     if sort_by not in valid_field:
#         raise HTTPException(status_code=404,detail="Not Found in valid field")
#     if order not in ["asc","des"]:
#         raise HTTPException(status_code=404,detail="Not Found in valid order")
#     data = load_data()

    