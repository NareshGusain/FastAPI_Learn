from fastapi import APIRouter, status, HTTPException, Depends
from db import Session,engine
from schemas import SignUpModel,LoginModel
from models import Users
from werkzeug.security import generate_password_hash, check_password_hash
from fastapi_jwt_auth import AuthJWT
from fastapi.encoders import jsonable_encoder

auth_router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

session  = Session(bind = engine)


@auth_router.get('/')
def hello(Authorize:AuthJWT=Depends()):
    try:
        Authorize.fresh_jwt_required()
    
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid token")

    return {"Message": "hello world"}


@auth_router.post('/signup',response_model=SignUpModel,status_code=status.HTTP_201_CREATED)
def signup(user:SignUpModel):
    db_email = session.query(Users).filter(Users.email == user.email).first()

    if not db_email:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with email already exists")

    db_username = session.query(Users).filter(Users.username == user.username).first()

    if not db_email:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with username already exists")   


    new_user = Users(
        username = user.username,
        email = user.email,
        password = generate_password_hash(user.password),
        is_staff = user.is_staff,
        is_active = user.is_active,
    ) 

    session.add(new_user)
    session.commit()

    return new_user


#login route
@auth_router.post('/login',status_code=200)
async def login(user:LoginModel,Authorize:AuthJWT=Depends()):
    """     
        ## Login a user
        This requires
            ```
                username:str
                password:str
            ```
        and returns a token pair `access` and `refresh`
    """
    db_user=session.query(Users).filter(Users.username==user.username).first()

    if db_user and check_password_hash(db_user.password, user.password):
        access_token=Authorize.create_access_token(subject=db_user.username)
        refresh_token=Authorize.create_refresh_token(subject=db_user.username)

        response={
            "access":access_token,
            "refresh":refresh_token
        }

        return jsonable_encoder(response)
    #else case
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
        detail="Invalid Username Or Password"
    )