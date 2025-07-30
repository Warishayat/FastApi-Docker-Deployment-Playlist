from pydantic import BaseModel,EmailStr,Field,field_validator
from typing import List,Dict,Annotated,Optional

#Fiedlvalidator class usage in the pydantic

class data(BaseModel):
    name:str
    email:EmailStr   #we will check each email that contain the domain edu.pk
    age:int
    married:bool
    allegies: Optional[List[str]] = None
    contact_list : Annotated[Optional[Dict[str,str]],Field(default=None,max_digits=100)]

    @field_validator("email")
    @classmethod
    def email_validator(cls,value):
        valid_domain = ["edu.pk"]   #numl@edu.pk
        domain_name = value.split("@")[1]
        if domain_name not in valid_domain:
            raise ValueError("Not a educational domain.You are not registerd with us.")
        return value
    
    @field_validator("name")
    @classmethod
    def name_validator(cls,value):
        return value.upper()
    
patient_Data = {
    "name" : "waris",
    "email" : "numls22@edu.pk",
    "age" : 22,
    "married" : False,
}

request = data(**patient_Data)
print(request)

def insertData(user:data):
    print(user.email)
    print(user.name)

    print("i was checking the domain of the user")

insertData(request)