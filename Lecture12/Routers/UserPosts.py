from fastapi.routing import APIRouter
from Utils import Oauth
from Schemas.UserCredential import Posts
from fastapi import Depends,status,HTTPException
from Config.database import get_db
from sqlalchemy.orm import Session
from Models.PostModel import PostValidation
from Models.model import TokenData
from Utils import Oauth


router = APIRouter(
    prefix="/posts",
    tags = [" User Posts"]
)

#get all posts ,user_id:int=Depends(Oauth.get_current_user)
@router.get('/allposts')
async def allposts(db:Session=Depends(get_db)):
    # print(user_id)
    try:
        Usersposts = db.query(Posts).all()
        if Usersposts:
            return{
                "success" : True,
                "Data" : Usersposts
            }

        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail = "User Posts are not Avaialable"
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {str(e)}"
        )


# this route will ask use to login before creating the post
@router.post("/createpost")
async def create_post(payload:PostValidation,db:Session=Depends(get_db),token_data: TokenData = Depends(Oauth.get_current_user)):
    print(token_data.id)
    try:
        data = Posts(
            title = payload.title,
            content = payload.content,
            published = payload.published,
            user_id = token_data.id
        )
        db.add(data)
        db.commit()
        db.refresh(data)
        return data
    except Exception as e:
        db.rollback() 
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {str(e)}"
        )
    