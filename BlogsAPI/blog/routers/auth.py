from fastapi import APIRouter, Depends, HTTPException, status
import schemas, models, database, token
from sqlalchemy.orm import Session



router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

@router.post('/login')
def login(request: schemas.Login, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.email)
    if not user: #if user not found based on given email then raise error
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Invalid Credentials")
    
    if user.password == request.password: #matching password
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Incorrect passord")
    
    
    access_token = token.create_access_token(data={"sub": user.email})
    return schemas.Token(access_token=access_token, token_type="bearer")
