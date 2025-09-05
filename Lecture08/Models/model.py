from pydantic import BaseModel,EmailStr


class ValidateSignup(BaseModel):
    name:str
    email:EmailStr
    password:str

class SignupResponse(BaseModel):
    id:int
    name:str
    email:EmailStr

    class Config:
        from_attributes = True

class ValidateLogin(BaseModel):
    email:EmailStr
    password:str

class LoginResponse(BaseModel):
    id:int
    email:EmailStr

    class Config:
       from_attributes = True
