from fastapi import FastAPI
app=FastAPI()

@app.get("/")
def root():
    return{"message": "hello"}

@app.get('/items/')
def read_root():
    return {"items":["item1","item2","item3"]}

@app.get('/items/{item_id}')
def read_root(item_id: str):
    return {"item": item_id}
