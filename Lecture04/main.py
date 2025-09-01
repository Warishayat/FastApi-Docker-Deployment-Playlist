from fastapi import FastAPI,HTTPException,responses,status
from fastapi.params import Body
import random
from Model.UserModel import CreatUser,UpdateUser

app = FastAPI(
    title="Practise of AI Powerd Apis",
    description = "This is all about the description you just need to know what to" \
    "use and how to use",
    version= "0.1.2"
)


posts = [
    {"id":1 , "name" : "waris hayat abbasi","Department":"AI Engineer","rollnum":12,"course":"Software Enginner"},
    {"id":2 , "name" : "Kashan Mehfooz Ali","Department":"Real Estate Agency","rollnum":13,"course":"Digital Marketing"},
    {"id":3 , "name" : "Wakar Zakka","Department":"Trading","rollnum":14,"course":"Trading On Harvard School of Business"}
]


@app.get("/ping")
async def pong():
    return{
        "success" : True,
        "message" : "pong"
    }



@app.get("/posts")
async def getallPost():
    return{
        "success" : True,
        "data"  : posts
    }



# Get a specific user
def findUser(id):
    for post in posts:
        if post["id"] == id:
            return post
    return None

@app.get("/posts/{id}")
async def get_specific_user(id: int):
    print(f'OK! Your Database id: {id}')
    data = findUser(id)
    print(data)
    if data == None:
        return {
            'success': False,
            'message': f"User not found corresponding to id {id}"
        }
    return {
        'success': True,
        'message': data
    }

#Create a New User in the database
@app.post("/createuser")
async def newUser(user:CreatUser):
    print(f"The new User Data is : {user}")
    data = user.dict()
    data["id"] = random.randint(1, 1000000)
    posts.append(data)
    return {
        "sucess" : True,
        "message" : "User has been Created Successfully",
        "data" : posts 
    }


#Update the post
def UpdateStudent(id:int):
    for key,value in enumerate(posts):
        if value['id'] == id:
            return key         #index
    return None

@app.put("/updateuser/{id}")
async def Update(id:int ,user:UpdateUser):
    print(f"User id is:{id}")
    data = user.dict()
    response=UpdateStudent(id=id)
    if response == None:
        return{
            "success" : False,
            "Message" : "Someything Went Wrong User id or something is wrong"
        }
    data["id"] = id
    posts[response] = data
    return {
        "success" : True,
        "message" : "User data has been updated Successfully"
    }


#deleted the user
def findUserAndDelete(id:int):
    for key,value in enumerate(posts):
        if value["id"] == id:
            return key
    return None


@app.delete("/deletuser/{id}")
async def UserDelet(id:int):
    data = findUserAndDelete(id)
    if data == None:
        return{
            "success" : True,
            "message" : "User is not crospond to this id"
        }
    posts.pop(data)
    return {
        "success" : True,
        "message" : "Post has been deleted Successfully."
    }




