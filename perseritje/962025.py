from fastapi import FastAPI

app=FastAPI()

@app.get ("/items/")
def read_items():
    return{"items":["item1","item2","item3"]}

@app.post ("/items/")
def create_items(name: str, price: float):
    return{"item_name":name, "item_price":price}