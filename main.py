from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app import database, crud, schemas

app = FastAPI()

def create_db_and_tables():
    #sql_app.database.Base.metadata.create_all(bind=engine)    
    database.Base.metadata.create_all(database.engine)

if __name__ == "__main__":
    print("Tentando criar as tabelas")
    create_db_and_tables()
    print("Criou as tabelas")

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        print("Criou a sessão")
        yield db
    finally:
        db.close()



@app.get("/producao/", response_model=list[schemas.Producao])
def read_producaos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    producoes = crud.get_producaos(db, skip=skip, limit=limit)
    return producoes


@app.get("/producao/{producao_id}", response_model=schemas.Producao)
def read_producao(producao_id: int, db: Session = Depends(get_db)):
    db_producao = crud.get_producao(db, user_id=producao_id)
    if db_producao is None:
        raise HTTPException(status_code=404, detail="Produção não encontrada")
    return db_producao





@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items