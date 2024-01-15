from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Todo
from models import TodoCreate  # Import the new Pydantic model


# ('app = FastAPI()' line se aapne ek naya FastAPI application banaya hai. 
# Ismein saare API endpoints aur dependencies honge.)
app = FastAPI()


# ('get_db' ek dependency function hai, jo har request ke liye ek naya database session provide karta hai. 
# 'SessionLocal' ka use iske liye kiya jata hai.)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ('/' endpoint par 'root' function hai jo ek welcome message return karta hai.)
@app.get("/")
def root():
    return {"message": "TODO API"}


# ('/todos/' endpoint par 'get_todos' function hai jo saare todos ko database se fetch karke return karta hai.)
@app.get("/todos/")
def get_todos(db: Session = Depends(get_db)):
    return db.query(Todo).all()


# ('/todos/' par POST request aane par, 'create_todo' function naya todo create karta hai aur use database mein save karta hai.)
@app.post("/todos/", response_model=TodoCreate)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    db_todo = Todo(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


# ('/todos/{todo_id}' par PUT request aane par, 'update_todo' function todo ko update karta hai aur updated todo ko return karta hai.)
@app.put("/todos/{todo_id}", response_model=TodoCreate)
def update_todo(todo_id: int, updated_todo: TodoCreate, db: Session = Depends(get_db)):
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    for key, value in updated_todo.dict().items():
        setattr(db_todo, key, value)
    db.commit()
    return TodoCreate(**db_todo.dict())


# ('/todos/{todo_id}' par DELETE request aane par, 'delete_todo' function todo ko delete karta hai.)
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(db_todo)
    db.commit()
    return {"message": f"Todo {todo_id} deleted"}