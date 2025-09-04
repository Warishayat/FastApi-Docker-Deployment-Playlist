from pydantic import BaseModel

class ModelResponse(BaseModel):
    name:str
    email:str

    class config:
        orm_mode=True