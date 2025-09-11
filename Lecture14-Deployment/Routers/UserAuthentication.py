from fastapi import APIRouter,HTTPException,Depends,status
from Utils.Oauth import verifyPassword,hashPassword,Create_Acess_token
from Models.model import ValidateSignup,SignupResponse,ValidateLogin
from Schemas.UserCredential import UserCredentialsData
from Config.database import get_db
from sqlalchemy.orm import Session
from typing import List
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(
    prefix="/user",
    tags=["Login/Signup"]
)



@router.post("/signup",response_model=SignupResponse)
async def UserSigninHandle(data:ValidateSignup,db:Session = Depends(get_db)):
    # few things will be here validate the frontend data
    # query data to check email is exist if exist sent httpException
    # if email not found create a new user with hash password and return back the responseModel to user
    existing_data = db.query(UserCredentialsData).filter(UserCredentialsData.email == data.email).first()
    if existing_data:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail =  "User already Exist"
        )
    hashedPassword = hashPassword(data.password)
    newUser = UserCredentialsData(
        name = data.name,
        email = data.email,
        password = hashedPassword
    )
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    return newUser



#Login ,response_model=LoginResponse
@router.post("/login")
async def LoginHandle(form_data: OAuth2PasswordRequestForm = Depends(),db:Session=Depends(get_db)):
    # Steps to follow
    # Always first check the email user is passing for login is existing or not in database
    existingUser = db.query(UserCredentialsData).filter(UserCredentialsData.email == form_data.username).first()
    if not existingUser:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Credential are invalid" 
        )
    verify_hahsed = verifyPassword(form_data.password,existingUser.password)

    if not verify_hahsed:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail = "Invalid Credetials"
        )

    access_token = Create_Acess_token(data={"user_id":existingUser.id})
    return {
        "access_token" : access_token,
        "token_type" : "Bearer"
    }