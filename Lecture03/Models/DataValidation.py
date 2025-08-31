from pydantic import BaseModel,EmailStr

# For Signup User
class SignupUser(BaseModel):
    name:str
    email:EmailStr
    password:str


# validation for Login
class LoginUser(BaseModel):
    email:EmailStr
    password:str