
from fastapi import FastAPI
from models import Developer, Project

app = FastAPI()

@app.post("/developers/")
def create_developer (developer: Developer):
    return {"message": "Developer created successfully", "developer": developer}
@app.post("/projects/")
def create_project (project: Project):
    return{"message": "Project created successfully", "Project": project}