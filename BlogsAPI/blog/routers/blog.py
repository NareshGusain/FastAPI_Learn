from typing import List
from os import path
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
import schemas, database, models


get_db = database.get_db
router = APIRouter(
    prefix='/blog',
    tags=['blogs']
)


#to retrive all blogs
@router.get('/', response_model=List[schemas.showBlog])
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


# to add new blog
@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title = request.title , body= request.body, user_id = 1)

    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


#to delete blog with ID
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def deletebyId(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).delete(models.Blog.id == id)
    
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"blog with id {id} not found")
    blog.delete(synchronize_session = False)
    db.commit()
    return 'deleted'


# to update blog with ID
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request: schemas.Blog , db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).update(request)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"Blog with id {id} not found")

    blog.update(request)
    db.commit()
    return 'updated'


# to get blog with ID
@router.get('/{id}', status_code= 200, response_model= schemas.showBlog)
def blogbyId(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code= 404, responses= f"blog with {id} not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return f"blog with {id} not found"
    return blog
