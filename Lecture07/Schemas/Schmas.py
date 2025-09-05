from pydantic import BaseModel

class ModelResponse(BaseModel):
    name: str
    email: str

    class Config:
        from_attributes = True