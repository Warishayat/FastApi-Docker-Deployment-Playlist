from pydantic import BaseModel


class ValidatePost(BaseModel):
    name:str
    roll:int
    room:int
    department:str
