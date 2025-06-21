
from fastapi import FastAPI
from models import Developer, Project

app = FastAPI()

@app.post("/developers/")
def create_developer (developer: Developer):
    return {"message": "Developer created successfully", "developer": developer}
@app.post("/projects/")
def create_project (project: Project):
    return{"message": "Project created successfully", "Project": project}

@app.get("/projects/")
def get_project():
    sample_project = Project(
        title = "sample project",
        description = "this is a sample project",
        language = ["python","javascript"],
        lead_developer = Developer(name="Jon Doe", experience=5)
    )
    return {"Project":[sample_project]}