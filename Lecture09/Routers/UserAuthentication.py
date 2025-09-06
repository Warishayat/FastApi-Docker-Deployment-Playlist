from fastapi import APIRouter,HTTPException,Depends
from Utils.Oauth import verifyPassword,hashPassword,Create_Acess_token
from Models.model import ValidateSignup,SignupResponse,LoginResponse,ValidateLogin
from Schemas.UserCredential import UserCredentialsData
from Config.database import get_db
from sqlalchemy.orm import Session
from typing import List


router = APIRouter(
    prefix="/User",
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
            status_code = 400,
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
async def LoginHandle(data:ValidateLogin,db:Session=Depends(get_db)):
    # Steps to follow
    # Always first check the email user is passing for login is existing or not in database
    existingUser = db.query(UserCredentialsData).filter(UserCredentialsData.email == data.email).first()
    if not existingUser:
        raise HTTPException(
            status_code = 404,
            detail = "Credential are invalid" 
        )
    verify_hahsed = verifyPassword(data.password,existingUser.password)

    if not verify_hahsed:
        raise HTTPException(
            status_code=404,
            detail = "Invalid Credetials"
        )
    
    #if password and email both match then make jwt token will let see in next class
    # for now we just sent the successfull response to welcome you are login.
    # 9/6/2025 i will handle the token now
    access_token = Create_Acess_token(data={"user_id":existingUser.id})
    return {
        "access_token" : access_token,
        "token_type" : "Bearer"
    }