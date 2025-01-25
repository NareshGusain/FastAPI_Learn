from fastapi import FastAPI
import uvicorn
import models
from database import engine
from routers import blog, users
# from passlib.context import CryptContext


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(blog.router)
app.include_router(users.router)



#pwd_cxt = CryptContext(schemes=['bcrypt'] , deprecated = 'auto')


if __name__ == "__main__":
    uvicorn.run("main:app")