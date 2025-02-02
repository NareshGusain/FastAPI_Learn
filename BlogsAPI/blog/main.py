from fastapi import FastAPI
import uvicorn
import models
from database import Base,engine
from routers import blog, users, auth
# from passlib.context import CryptContext

models.Base.metadata.create_all(bind=engine)


app = FastAPI()


app.include_router(blog.router)
app.include_router(users.router)
app.include_router(auth.router)

#pwd_cxt = CryptContext(schemes=['bcrypt'] , deprecated = 'auto')


if __name__ == "__main__":
    uvicorn.run("main:app")

# uvicorn main:mainApp --reload