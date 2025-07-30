# Developed a api in the fastapi

# End point for creatinf the pateint mean post request
# view the record of the patient
# particular patient ka profile dekh lo
# particular pateint ko update krlo
# patient ko dlt kar do.


#Q: what is software -> dynamic and static  ->static mean no chnges on the screen while dynamic user can intract with it.


# lets make a basic api

from fastapi import FastAPI
import json

app = FastAPI()

def load_data():
    with open("patient.json","rb") as f:
        data = json.load(f)
    return data


#route1
@app.get("/")
async def hello():
    return{
        "message":"Welcome to the fetch data of the aptient"
    }

#Route2

@app.get("/about")
async def about():
    return {
        "message" : "get the full record of the patient."
    }

@app.get("/view")
async def viewAll():
    data = load_data()
    return data


