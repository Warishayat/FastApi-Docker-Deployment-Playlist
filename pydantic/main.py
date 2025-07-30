# why pydantic it solve two main probelm


# problem 1: Typed Validation

# def insertData(name,age):
#     # save this data into the database
#     print(name)
#     print(age)

#     print("suppose these twoa re inserted into the database.")

# # this is the function and supppose that soemnew user use the same function and pass the data instead og age into number its
# # passing into the string that is getting stored in the database .that is a big probelm for that we will use pydantic clases 
# # for it

# # type hinting 
# # def insert(name:str,age:int):
# #     if type(name) == str and type(age) == int:
# #         return name,age
# #     else:
# #         return TypeError
# # print(insert("waris","12"))

# # suppose we are using someother function  like for update we need to pass this code sasme as it.

# # Problem 2 : Data validation
# #  in last code we handle the type validation now what is data validation like i want age should not be negative .
# # def insert0(name:str,age:int):
# #     if type(name) == str and type(age) == int:
# #         if age < 0:
# #             raise ValueError("Tum value negatie nai de skte mittar.")
# #         else:
# #             return name,age
# #     else:
# #         return TypeError("Sahi sahi data bhj na dost mery")
    
# # print(insert0("kashan",18))

# # pydantic solve the saeme problem its want there should be no problem related validation and type error.
# # lets dicuss how it work
# # 1 : build a class in pydantic and define schema of class in it 
# # 2 : Raw input se instantiate karte hn -->pydantic object and its object is validated.
# # 3 : step 3 m function k pas bhj detay ho.


# # lets code the pydantiic class

# #install pydantic by pip

# # STEP 1 : Make the pydantic lass and schema
# from pydantic import BaseModel

# class patient(BaseModel):
#     name:str
#     age:int
    



# patient_info = {"name":"waris","age":30}  
# #step2 make the object of the pydantic class
# pateint1 = patient(**patient_info)


# #Step 3
# # function k pass bhj do is object ko
# def insert_Data(user:patient):
#     print(user.name)
#     print(user.age)

#     print('Assume your data is stored in the database.')


# def update_data(user:patient):
#     print("user",user.name)
#     print("age",user.age)
#     print("updated has been made.")
# update_data(pateint1)


# Typed  Validation

from pydantic import BaseModel,EmailStr,Field
from typing import List,Dict,Optional,Annotated

class data(BaseModel):
    name:Annotated[str,Field(max_length=5,title="name of the patient",description="Enter the naem of pateint in 5 character",examples="ex:waris")]
    email:EmailStr     #Email data validation
    age:int = Field(gt=0,lt=60)
    married:bool
    weight : float = Field(gt=0)
    allergies : Optional[List[str]] = None  #if some field want optional than we can make it optional.
    contact : Annotated[Dict[str],Field(default=None,max_length=50)]


patient_data = {
    "name": "waris",
    "email" : "warishayat666@gmail.com",
    "age":10,
    "married": True,
    "weight": 12.2,
    # "allergies": ["asthma", "maleria", "goodfit"],
    # "contact": {"ph1": "03132737"}
}

patient1 = data(**patient_data)


def insertdata(user:data):
    print(user.name)
    print(user.email)
    print(user.age)
    print(user.married)
    print(user.allergies)
    print(user.contact)
    print(user.weight)
    print("All these classes are working fine")


def updateData(user:data):
    print(user.name)
    print(user.email)
    print(user.age)
    print(user.married)
    # print(user.allergies)
    # print(user.contact)
    print(user.weight)
    print("Alldata is updated fine")

# print(insertdata(patient1))
print(updateData(patient1))



# Pydantic data validation
