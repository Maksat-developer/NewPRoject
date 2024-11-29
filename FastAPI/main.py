from fastapi import FastAPI
from database import Base, engine
from models import Todo
from schemas import TodoReq
from sqlalchemy.orm import Session

Base.metadata.create_all(engine)

app = FastAPI()


@app.post('/todo/create/')
def create_todo(todo : TodoReq):
    session = Session(bind=engine, expire_on_commit=False)
    todo_db = Todo(title=todo.title, completed=todo.completed)
    session.add(todo_db)
    session.commit()
    session.close()
    return 'Succesfuly created'


@app.get('/todo/')
def todo():
    session = Session(bind=engine, expire_on_commit=False)
    todo = session.query(Todo).all()
    return todo


@app.put('/todo/{id}/')
def todo_update(id:int, name:str, completed:bool):
    session = Session(bind=engine, expire_on_commit=False)
    todo = session.query(Todo).get(id)
    if todo:
        todo.title = name
        todo.completed = completed
        session.commit()
        session.close()
        return f"Successfuly updated"
    else:
        return "Error not found"


@app.delete('/todo/delete/{id}')
def delete_todo(id : int):
    session = Session(bind=engine, expire_on_commit=False)
    todo = session.query(Todo).get(id)
    if todo:
        session.delete(todo)
        session.commit()
        session.close()
        return "Succesfuly delete"
    else:
        return "Error id not found"






