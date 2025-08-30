from pydantic import BaseModel
from typing import Optional

class ValidatePOst(BaseModel):
    title:str
    content:str
    message:Optional[str] = None