from fastapi import APIRouter, Depends, HTTPException
import schemas, database, models
from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/user',
    tags=['users']
)
get_db = database.get_db


@router.post('/')
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    # hashedpassword = pwd_cxt(request.password)
    new_user = models.User(name = request.name, email = request.email, password = request.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user) #refresh on new user

    return new_user


@router.get('/{id}' , response_model=schemas.ShowUser)
def postbyID(id: int, db: Session = Depends(get_db)):
    # hashedpassword = pwd_cxt(request.password)
    new_user = db.query(models.User).filter(models.User.id == id).first()

    if not new_user:
        raise HTTPException(status_code=404, detail=f"User with id {id} not found")  
    db.add(new_user)
    db.commit()
    db.refresh(new_user) #refresh on new user

    return new_user