from pydantic import BaseModel
from typing import Optional

class PostValidation(BaseModel):
    title:str
    content:str
    published : Optional[bool]  = True
    # rating : Optional[str] = None