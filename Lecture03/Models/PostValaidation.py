from pydantic import BaseModel


class ValidatePost(BaseModel):
    name:str
    roll:int
    room:int
    department:str


class UpdateData(BaseModel):
    name:str
    roll:int
    room:int
    department : str