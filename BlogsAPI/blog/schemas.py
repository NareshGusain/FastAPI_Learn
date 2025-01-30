# pydantic models are nothing but schemas
# when we need to pydantic models and we define it under schemas.py
from pydantic import BaseModel
from typing import Optional, List

class BlogBase(BaseModel):
    title: str
    body: str

class Blog(BlogBase):
    title: str
    body: str
    published: Optional[bool] = True 

    class Config():
        from_attributes = True 


class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str
    blogs: list[Blog] = []
    class Config():
        from_attributes = True 

class showBlog(BaseModel):
    title:str
    body: str
    user_id: int  # ✅ Add user_id to match models.Blog
    published: Optional[bool] = True

    class Config():
        from_attributes = True


class Login(BaseModel):
    email: str #email
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None
    