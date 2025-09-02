#This lecture is all about the databases
# a database is the collection  onf organised data that can be easily
# Managable and retrived when need.


# user sent the req to the server and server sent that req to the database
# Databases type
# 1: Relational      2: NON Relational Databases
# We will mostly work with postgresql
# https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
# SQL is structures queery language where everyhting is structured.
# Postgres for window ------Installation 
# To install the database type the command ''

# What is table ----> it is subject or event ,table of the users that are
# registerd products that we have and purchase that we made in last 
# month. suppose a table of user ,priduct and purchase

# Then we have rows and columns cols contain name like age ,name ,adress etc.
# Row contain the data of the name like waris,islamabad pakistan,23
# Datatype -->What kind of datattype i want to use like name must be string
# Age must be a number same for others fields.

# In python we have two main type string and number

# Name: str = "waris hayat abbasi",
# Adrss : sgt= "Islamabad Pakistan",
# Age : int = 23

# Primary Key: in table we have primary key which uniquely identify the table mean id,email etc
# we only have only one primary key in the table.
# UNIQUE: Some Colum can be unique like email can be unique two user canott signup with the sam accouny
# NULL :  we can take some value as default.
#  Lets practise on pg admin
import psycopg2   
from psycopg2.extras  import RealDictCursor 
from fastapi.exceptions import HTTPException 
from fastapi import FastAPI,Response,status
from Models.UserModel import PostValidation
import time
from dotenv import load_dotenv
import os

load_dotenv()

database_name = os.environ.get("database_name")
password = os.environ.get("password")
host_name = os.environ.get("localhost_name")

app = FastAPI(
    title="AI Powerd Application of Multiple Api's",
    description = "This lecture is all about the Apis for macahine learning.",
    version = "1.0.4" 
)

# Connect Database 
while True:
    try:
        conn = psycopg2.connect(host="localhost",database='fastapi',user='postgres',password='waris4200',cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successfull")
        break
    except Exception as e:
        print(f"you have some error at {e}")
        time.sleep(2)
        

@app.get("/")
def ping():
    return 
    {
        "success" : True,
        "message" : "You are looking for pong"
    }


#get all post from database
@app.get("/posts")
async def getallposts():
    cursor.execute(''' SELECT * FROM posts''')
    allpost=cursor.fetchall()
    if allpost:
        return{
            "code" : 200,
            "success" : True,
            "message" : allpost
        }
    return{
        "success" : False,
        "message" : "No post found in the database"
    }


#creat a brand new post
@app.post("/creatpost")
async def newpost(user: PostValidation):
    cursor.execute(
        """INSERT INTO posts (title, content, published) VALUES (%s, %s, %s)""",
        (user.title, user.content, user.published)
    )
    conn.commit()
    return {"message": "Post Created Successfully"}


#get a single post
@app.get("/asinglepost/{id}")
async def getsinglePost(id:int):
    cursor.execute("SELECT * FROM posts WHERE id = %s", (id,))
    post = cursor.fetchone()

    if post:
        return{
            "success" : True,
            "data" : post
        }
    return{
        "success" : False,
        "message" : "User not found"
    }


#delet a post
@app.delete("/posts/{id}")
async def delete_post(id: int):
    cursor.execute("DELETE FROM posts WHERE id = %s RETURNING *", (id,))
    deleted_post = cursor.fetchone()
    conn.commit()  # Don’t forget to commit changes!

    if not deleted_post:
        raise HTTPException(status_code=404, detail="Post not found")

    return {
        "success": True,
        "message": "Post deleted successfully",
        "data": deleted_post
    }


#update a post 
@app.put("/posts/{id}")
async def update_post(id: int, post: PostValidation):
    cursor.execute(
        """
        UPDATE posts
        SET title = %s, content = %s, published = %s
        WHERE id = %s
        RETURNING *;
        """,
        (post.title, post.content, post.published, id)
    )
    updated_post = cursor.fetchone()
    conn.commit()

    if not updated_post:
        raise HTTPException(status_code=404, detail="Post not found")

    return {
        "success": True,
        "message": "Post updated successfully",
        "data": updated_post
    }