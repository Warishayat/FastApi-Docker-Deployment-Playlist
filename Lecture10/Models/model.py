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

class Token(BaseModel):
    access_token:str
    token_type:str

from typing import Optional
class TokenData(BaseModel):
    id : Optional[int] = None

