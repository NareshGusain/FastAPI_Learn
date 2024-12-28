from enum import Enum

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Category(Enum):
    TOOLS= "tools"
    CONSUMABLES = "consumables"

#BaseModel inheritance
class Item(BaseModel):
    name: str
    price: float
    count: int
    id: int
    category: Category

#DB
items = {
    0: Item(name= "Naresh",price=9.99 , count=10 , id=0, category=Category.TOOLS),
    1: Item(name= "Peter",price=5.99 , count=50 , id=1, category=Category.CONSUMABLES),
    2: Item(name= "Sam",price=6.32 , count=20 , id=2, category=Category.TOOLS),
    3: Item(name= "joe",price=10.56 , count=30 , id=3, category=Category.CONSUMABLES)
} 



@app.get("/")
def index() -> dict[str, dict[int, Item]]:
    return {"items": items}

@app.get("/items/{item_id}")
def query_item_by_id(item_id: int) -> Item:
    if item_id not in items:
        raise HTTPException(status_code=404, detail =f"Item with {item_id} does not exist.")
    else:
        return items[item_id] # converting into json is handle by fast api
    
Selection = dict[
    str, str | int | float | Category | None
    # dict containing user query arguments 
]

@app.get("/items/")
def query_items_by_parameters(
    name: str | None = None,
    price: float | None = None,
    count: int | None = None,
    id: int | None = None,
    category: Category | None = None,
    ) -> dict[str, Selection]:

    #helper function
    def check_item(item: Item) -> bool:
        return all(
            (
                name is None or item.name == name,
                price is None or item.price == price,
                count is None or item.count != count,
                category is None or item.category is category,
            )
        )
    selection  = [item for item in items.values() if check_item(item)]
    return {
        "query" : {"name" : name , "price": price, "count": count, "category": category},
        "selection" : selection
    }

@app.post("/")
def add_item(item: Item) -> dict[str , Item]:
    if item.id in items:
        HTTPException(status_code=400 , detail=f"Item with item {item.id=} already exist.")

    items[item.id] = item
    return {"added": item}


@app.put("/update/{item_id}")
def update(
    item_id: int,
    name: str | None = None,
    price: float | None = None,
    count: int | None = None,
) -> dict[str, Item]:
    
    if item_id not in items:
        HTTPException(status_code=404 , detail=f"Item with item {item_id=} does not exist.")
    if all(info is None for info in (name,price,count)):
        raise HTTPException(status_code=400 , detail="No parameters provided for update.")
    
    item = items[item_id]
    if name is not None:
        item.name = name
    if price is not None:
        item.price = price
    if count is not None:
        item.count = count

    return {"updated": item}

@app.delete("/delete/{item_id}")
def delete_item(item_id: int) -> dict[str, Item]:

    if item_id not in items:
        raise HTTPException(
            status_code=404, detail=f"Item with {item_id=} does not exist."
        )

    item = items.pop(item_id)
    return {"deleted": item}