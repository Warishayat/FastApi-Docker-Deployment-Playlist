from fastapi import FastAPI,Response,status,HTTPException
from fastapi.params import Body
from Models.PostValaidation import ValidatePost



app = FastAPI(
    title="AI powerd Application",
    description="This Application is all about the ai and machine learning you can test these api's with your system",
    version='1.0.2'
)

my_posts = [
    {"name":"waris hayat abbasi","roll":21368, "room":512 , "department":"Software Engineering","id":1},
    {"name":"Asif hayat abbasi","roll":21668, "room":512 , "department":"Software Engineering","id":2}
    ]



#Root Route 
@app.get("/")
async def root():
    return {
        "message" : "Hello world"
    }


# get all post
@app.get("/posts")
def get_posts():
    return {
        "data" : my_posts
    }

# Creat Post
@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_users(post:ValidatePost):
    my_posts.append(post.dict())
    return {
        
        "messgae": "Successfully post has been creatd",
        "Post" : my_posts
    }



#get a single post
def findpost(id):
    for p in my_posts:
        if p['id'] == id:
            return p
    return {"Post Not Found"}


@app.get("/posts/{id}")
async def get_post(id: int):
    post = findpost(id)  
    if post != {"Post Not Found"}:
        return {
            "success": True,
            "Post": post
        }
    return {
        "success": False,
        "Post": f"{post}"
    }


def deletPost(id):
    for i,p in enumerate(my_posts):
        if p['id'] == id:
            return i
        return None


@app.delete("/postdel/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def delet_post(id: int):
    remove_post = deletPost(id)
    if remove_post is None:   
        raise HTTPException(
            status_code=404,
            detail=f"Post with id {id} not found."
        )
    my_posts.pop(remove_post)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

#put or patch request 


# Now this lecture is all about crud operation. (Creat retrive update  and Delete).
