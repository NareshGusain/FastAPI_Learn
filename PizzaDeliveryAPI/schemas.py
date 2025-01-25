from typing import Optional
from pydantic import BaseModel, EmailStr
from pydantic import BaseSettings, SettingsConfigDict

class SignUpModel(BaseModel):
    id: Optional[int] = None  # Optional integer field
    username: str  # Required string field
    email: str  # Validated email field
    password: str  # Required string field
    is_staff: Optional[bool] = False  # Optional boolean field with default value
    is_active: Optional[bool] = True  # Optional boolean field with default value

    model_config = {
        "from_attributes": True,  # Use for ORM support in Pydantic v2
        "json_schema_extra": {  # Additional schema information
            "example": {
                "username": "johndoe",
                "email": "johndoe@gmail.com",
                "password": "password",
                "is_staff": False,
                "is_active": True
            }
        }
    }

class Settings(BaseModel):
    authjwt_secret_key:str = 'b4bb9013c1c03b29b9311ec0df07f3b0d8fd13edd02d5c45b2fa7b86341fa405'

class LoginModel(BaseModel):
    username: str
    password:str
    

def Ordermodel(BaseModel):
    id:Optional[int]
    quantity:int
    order_status:Optional[str]="PENDING"
    pizza_size:Optional[str]="SMALL"
    user_id:Optional[int]


    class Config:
        orm_mode=True
        schema_extra={
            "example":{
                "quantity":2,
                "pizza_size":"LARGE"
            }
        }