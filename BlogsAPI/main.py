from fastapi import FastAPI
from typing import Optional
import uvicorn
import models

app = FastAPI()

@app.get('/blog')
def index(limit=10 , published:bool=True, sort:Optional[str] = None):
    if published:
        return {'data': f"{limit} published blogs from the db"}
    else:
        return {'data': f'{limit} blogs from db'}


@app.get('/blog?limit=10&published=true')
def showLimited():
    return {'retrun':  "Blogssss"}

@app.get('/blog/{id}')
def show(id:int):
    return {'data':id}

@app.post('/blog')
def createBlog(request: models.Blog): 
    return {"data":f"Blog is create with {request.title}"}



if __name__ == "__main__":
    uvicorn.run("blog.main:app")