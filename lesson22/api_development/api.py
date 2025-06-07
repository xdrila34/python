from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User (BaseModel):
    id: int
    name: str
    age: int
    email: str
@app.post("/users/")

async def create_user(user: User):
    return user

class Person(BaseModel):
    name:str
    age:int

@app.post("/create_person")
async def create_person(person: Person):

    return{"message:" f"Person{person.name} created with age {person.age}
        
