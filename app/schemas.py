import time
from pydantic import BaseModel
from datetime import datetime

class ProducaoBase(BaseModel):
    id : int
    leitura : str
    produto_id : str | None = None
    descricao : str
    status_id : int
    local_id : str
    dt : datetime
    hr : time
    serie : str
    user_id : int
    setor_id : str
    os_id : int | None = None
    
    
class ProducaoCreate(ProducaoBase):
    pass

class Producao(ProducaoBase):
    id : int
    produto_id : str | None = None
    status_id : int
    local_id : str
    user_id : int
    setor_id : str
    os_id : int | None = None

    class Config:
        orm_mode = True

class ItemBase(BaseModel):
    title: str
    description: str | None = None

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True