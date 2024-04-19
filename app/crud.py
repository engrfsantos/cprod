from sqlalchemy.orm import Session

import app.models as models, app.schemas as schemas

def get_producao(db: Session, producao_id: int):
    return db.query(models.Producao).filter(models.Producao.id == producao_id).first()

def get_producaos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Producao).offset(skip).limit(limit).all()

def get_setor(db: Session, setor_id: str):
    return db.query(models.Setor).filter(models.Setor.id == setor_id).first()

def get_setors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Setor).offset(skip).limit(limit).all()

def get_proddefeito(db: Session, proddefeito_id: id):
    return db.query(models.ProdDefeito).filter(models.ProdDefeito.id == proddefeito_id).first()

def get_proddefeitos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ProdDefeito).offset(skip).limit(limit).all()


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item