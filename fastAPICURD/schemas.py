from pydantic import BaseModel


class PostBase(BaseModel):
    content: str
    title: str

    class Config:
        #to enable the data model to work in ORM mode, allowing it to be used with SQLAlchemy's ORM features.
        orm_mode = True


class CreatePost(PostBase):
    class Config:
        orm_mode = True