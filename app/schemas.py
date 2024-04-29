import time
from pydantic import BaseModel
from datetime import time, timedelta
from datetime import date

class ProducaoBase(BaseModel):
    id : int
    leitura : str
    produto_id : str | None = None
    descricao : str
    status_id : int
    local_id : str
    dt : date
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


class ProcessoBase(BaseModel):
    id : str
    desc_breve : str 
    descricao : str | None = None
    status_id : str | None = None
    local_id : str | None = None
    reparo : bool | None = None
    autoconfrede : bool | None = None
    burnin : bool | None = None
    fechaos : str | None = None
    obrpn : bool | None = None
    tipoid : str  | None = None
    
class ProcessoCreate(ProcessoBase):
    pass

class Processo(ProcessoBase):
    id : str
    desc_breve : str
    descricao : str 

    class Config:
        orm_mode = True

class DefeitoBase(BaseModel):
    id: int
    descricao: str 
    ean: str  | None = None
    grupo_id: str | None = None
    codigo_id: str | None = None
    agrupar: str | None = None
    categoria: str | None = None

class DefeitoCreate(DefeitoBase):
    pass

class Defeito(DefeitoBase):
    id: int 
    descricao: str
    
    class Config:
        orm_mode = True

class ProdDefeitoBase(BaseModel):
    id : int
    obs : str 
    acao : str | None = None
    status_id : int | None = None
    dt : date | None = None
    hr1 : time | None = None
    defeito : str | None = None
    hr1 : timedelta | None = None
    producao_id : int | None = None
    defeito_id : int | None = None
    timestamp : time | None = None
    bipagem : str  | None = None
    grupo_defeito_id: int 
    
class ProdDefeitoCreate(ProdDefeitoBase):
    pass

class ProdDefeito(ProdDefeitoBase):
    id : int
    obs : str | None = None
    acao : str | None = None
    status_id : int | None = None
    producao_id : int | None = None
    defeito_id : int | None = None
    bipagem : str  | None = None
    grupo_defeito_id: int | None = None
  
    class Config:
        orm_mode = True


class StatusBase(BaseModel):
    id : int
    desc_breve : str | None = None 
    descricao : str | None = None
    
class StatusCreate(StatusBase):
    pass

class Status(StatusBase):
    id : int
    desc_breve : str | None = None
    descricao : str | None = None
    
    class Config:
        orm_mode = True


class ProdutoBase(BaseModel):
    id: str 
    descricao: str 
    narrativa: str
    unidade: str 
    descricao_especifica: str 
    grupo: str 
    cod_barras: str 
    tipo: str 
    
class ProdutoCreate(ProdutoBase):
    pass

class Produto(BaseModel):
    id: str 
    descricao: str 
    grupo: str 
    cod_barras: str 
    tipo: str 

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