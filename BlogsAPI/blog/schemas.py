from pydantic import BaseModel
from typing import Optional, List

class BlogBase(BaseModel):
    title: str
    body: str

class Blog(BaseModel):
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
    creator: ShowUser

    class Config():
        from_attributes = True