from fastapi import APIRouter, Depends
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
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    # hashedpassword = pwd_cxt(request.password)
    new_user = models.User(name = request.name, email = request.email, password = request.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user) #refresh on new user

    return new_user