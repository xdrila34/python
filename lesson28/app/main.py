from fastapi import FastAPI, Depends, HTTPException
from typing import List
from .crud import create_item, get_items, get_item, update_item, delete_item
from .models import Item
from .security import get_api_key
from .database import init_db

app = FastAPI()

init_db()

@app.post("/items/", response_model=Item)
def create_new_item(item: Item, api_key: str=Depends(get_api_key)):
    return create_item()

@app.get("/items/", response_model=List[Item])
def read_items(api_key: str=Depends(get_api_key)):
    return get_items()

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int, api_key: str=Depends(get_api_key)):
    item = get_item(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        return item

@app.put("/items/{item_id}", response_model=Item)
def update_existing_item(item_id: int,item: Item, api_key: str=Depends(get_api_key)):
    updated_item = update_item(item_id, item)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        return updated_item

@app.delete("/items/{item_id}")
def delete_existing_item(item_id: int, api_key: str=Depends(get_api_key)):
    result = delete_item(item_id)
    if not result:
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        return {"detail": "Item deleted successfully"}