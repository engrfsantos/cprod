from sqlalchemy.orm import Session

import app.models as models, app.schemas as schemas

def get_producao(db: Session, producao_id: int):
    return db.query(models.Producao).filter(models.Producao.id == producao_id).first()

def get_producaos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Producao).offset(skip).limit(limit).all()

def get_processo(db: Session, processo_id: str, local_id: str):
    print("Processo", processo_id, "Local", local_id)
    return db.query(models.Processo).filter(models.Processo.id == processo_id, models.Processo.local_id==local_id).first()

def get_processos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Processo).offset(skip).limit(limit).all()

def get_defeito(db: Session, defeito_id: id):
    return db.query(models.Defeito).filter(models.Defeito.id == defeito_id).first()

def get_defeitos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Defeito).offset(skip).limit(limit).all()

def get_proddefeito(db: Session, proddefeito_id: id):
    return db.query(models.ProdDefeito).filter(models.ProdDefeito.id == proddefeito_id).first()

def get_proddefeitos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ProdDefeito).offset(skip).limit(limit).all()

def get_status(db: Session, status_id: str):
    return db.query(models.Status).filter(models.Status.id == status_id).first()

def get_statuss(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Status).offset(skip).limit(limit).all()

def get_produto(db: Session, produto_id: str):
    return db.query(models.Produto).filter(models.Produto.id == produto_id).first()

def get_produtos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Produto).offset(skip).limit(limit).all()

def get_usuario(db: Session, usuario_id: str):
    return db.query(models.Usuario).filter(models.Usuario.re == usuario_id).first()

def get_usuarios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Usuario).offset(skip).limit(limit).all()

def get_grupo(db: Session, grupo_id: str):
    return db.query(models.Grupo).filter(models.Grupo.id == grupo_id).first()

def get_grupos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Grupo).offset(skip).limit(limit).all()

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