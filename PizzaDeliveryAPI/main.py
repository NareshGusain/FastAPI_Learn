import uvicorn
from fastapi import FastAPI
from auth_routes import auth_router
from order_routes import order_router
from fastapi_jwt_auth import AuthJWT
from schemas import Settings


app = FastAPI()


#this will create and instance of setting class
@AuthJWT.load_config
def get_config():
    return Settings()

app.include_router(auth_router)
app.include_router(order_router)


@app.get('/')
def hello():
    return {'main': "world"}


if __name__ == "__main__":
    uvicorn.run("main:app")
