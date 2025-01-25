from pydantic import BaseModel
from typing import Optional

class Blog(BaseModel):
    __tablename__ = "blogs"

    title: str
    body: str
    published: Optional[bool] = True 

    