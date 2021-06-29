from fastapi import FastAPI
from pydantic import BaseModel

class Task(BaseModel):
    title:str
    completed:bool

app = FastAPI ()

ToDoList =[]

@app.on_event("startup")
async def startup():
    ToDoList.append(Task( title="Install Python 3.6+" , completed=True))
    ToDoList.append(Task( title="Install fastAPI" , completed=True))
    ToDoList.append(Task( title="Install Uvicorn" , completed=True))
    ToDoList.append(Task( title="Develop REST API", completed=False))
    ToDoList.append(Task( title="Delete this task", completed=False))

@app.get("/tasks")
async def get_all_tasks():
    return ToDoList

@app.post("/tasks" , status_code=201)
async def create_task(item:Task):
    ToDoList.append(item)
    return ToDoList[-1]

@app.delete("/tasks/{index}")
async def delete_task(index:int):
    ToDoList.pop(index)
    return {}
