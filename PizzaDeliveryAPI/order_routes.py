from fastapi import APIRouter

order_router = APIRouter(
    prefix='/orders',
    tags= ['orders']
)

@order_router.get('/')
def hello():
    return {'order': "world"}