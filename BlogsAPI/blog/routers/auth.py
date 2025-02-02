from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
import schemas, models, database
import auth_token
from sqlalchemy.orm import Session



router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.email).first()
    if not user: #if user not found based on given email then raise error
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User does not exist")
    
    if user.password != request.password: #matching password
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Incorrect password")
    
    # everything is fine, create accestoken
    access_token = auth_token.create_access_token(data={"sub": user.email})
    return schemas.Token(access_token=access_token, token_type="bearer")
