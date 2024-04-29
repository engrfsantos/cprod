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
    db_producao = crud.get_producao(db, producao_id=producao_id)
    if db_producao is None:
        raise HTTPException(status_code=404, detail="Produção não encontrada")
    return db_producao

@app.get("/processo/", response_model=list[schemas.Processo])
def read_processoss(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    processos = crud.get_processos(db, skip=skip, limit=limit)
    return processos

@app.get("/processo/{local_id}/{processo_id}", response_model=schemas.Processo)
def read_processo(processo_id: str, local_id: str, db: Session = Depends(get_db)):
    print("Processo ",processo_id , "Local", local_id)
    db_processo = crud.get_processo(db, processo_id=processo_id, local_id=local_id)
    if db_processo is None:
        raise HTTPException(status_code=404, detail="Processo não encontrado")
    return db_processo

@app.get("/defeito/", response_model=list[schemas.Defeito])
def read_defeitos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    defeitos = crud.get_defeitos(db, skip=skip, limit=limit)
    return defeitos

@app.get("/defeito/{defeito_id}", response_model=schemas.Defeito)
def read_defeito(defeito_id: int, db: Session = Depends(get_db)):
    db_defeito = crud.get_defeito(db, proddefeito_id=defeito_id)
    if db_defeito is None:
        raise HTTPException(status_code=404, detail="Defeito não encontrado")
    return db_defeito


@app.get("/proddefeito/", response_model=list[schemas.ProdDefeito])
def read_proddefeitos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    proddefeitos = crud.get_proddefeitos(db, skip=skip, limit=limit)
    return proddefeitos

@app.get("/proddefeito/{proddefeito_id}", response_model=schemas.ProdDefeito)
def read_proddefeito(proddefeito_id: int, db: Session = Depends(get_db)):
    db_proddefeito = crud.get_proddefeito(db, proddefeito_id=proddefeito_id)
    if db_proddefeito is None:
        raise HTTPException(status_code=404, detail="Setor não encontrado")
    return db_proddefeito

@app.get("/status/", response_model=list[schemas.Status])
def read_statuss(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    setors = crud.get_statuss(db, skip=skip, limit=limit)
    return setors

@app.get("/status/{status_id}", response_model=schemas.Status)
def read_status(status_id: str, db: Session = Depends(get_db)):
    db_setor = crud.get_status(db, status_id=status_id)
    if db_setor is None:
        raise HTTPException(status_code=404, detail="Setor não encontrado")
    return db_setor


@app.get("/produto/", response_model=list[schemas.Produto])
def read_produtos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    produtos = crud.get_produtos(db, skip=skip, limit=limit)
    return produtos

@app.get("/produto/{produto_id}", response_model=schemas.Produto)
def read_produto(produto_id: str, db: Session = Depends(get_db)):
    db_produto = crud.get_produto(db, produto_id=produto_id)
    if db_produto is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return db_produto


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