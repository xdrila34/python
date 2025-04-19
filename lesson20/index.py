from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def root():
    return {"message:helloworld"}

@app.get("/greet/")
def read_root(name: str):
    return{"message": f"hello, {name}!"}