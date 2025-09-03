from pydantic import BaseModel
from typing import Optional



class ValidateUser(BaseModel):
    title:str
    content:str
    published:Optional[bool]=True

class UpdateUserValidation(BaseModel):
    title : Optional[str]
    content : Optional[str]
    published : Optional[bool]
