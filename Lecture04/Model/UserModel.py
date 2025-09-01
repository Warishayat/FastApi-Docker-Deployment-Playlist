import random
from pydantic import BaseModel
from typing import Optional


class CreatUser(BaseModel):
    name:str
    Department:str
    rollnum:int
    course : str


class UpdateUser(BaseModel):
    name:str
    Department:str
    rollnum:int
    course : str
