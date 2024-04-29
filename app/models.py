from sqlalchemy import Boolean, Column, Time, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

import datetime, time

from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.database import Base
 
class Producao(Base):
    __tablename__ = "td01_producao"
    id: int = Column("td01_producao_id",Integer, primary_key=True)    
    leitura: str = Column("td01_leitura",String)
    produto_id: str = Column("td01_cod_produto",String, ForeignKey("produto.id"))
    descricao: str = Column("td01_descricao",String)
    status_id: int = Column("td01_status",Integer, ForeignKey("statuss.id"))
    processo_id: str = Column("td01_id",String, ForeignKey("locais.id"))
    dt: datetime =  Column("td01_dt",DateTime, default=datetime.date)
    hr: time = Column("td01_hr",Time)
    serie: int = Column("td01_serie",Integer)
    user_id: int = Column("td01_re",Integer, ForeignKey("users.id"))
    setor_id: str = Column("td01_local",String, ForeignKey("setors.id"))
    os_id: int = Column("td01_os",Integer, ForeignKey("oss.id"))

class Status(Base):
    __tablename__ = "ts01_status"
    id: int = Column("ts01_status", Integer, primary_key=True, nullable=False)
    desc_breve: str = Column("ts01_desc_breve", String,nullable=False)
    descricao: str = Column("ts01_descricao", String,nullable=False)

class Processo(Base):
    __tablename__ = "td01_identificador"
    id: str = Column("td01_id",String, primary_key=True, nullable=False) #td01_id character varying(6) COLLATE pg_catalog."default" NOT NULL,
    desc_breve: str = Column("td01_desc_breve", String) #td01_desc_breve character varying(10) COLLATE pg_catalog."default" NOT NULL,
    descricao: str = Column("td01_descricao",String) #td01_descricao character varying(50) COLLATE pg_catalog."default",
    status_id: str = Column("td01_status",String) #td01_status character varying(2) COLLATE pg_catalog."default",
    local_id: str = Column("td01_local", String, primary_key=True, nullable=False ) #td01_local character varying(5) COLLATE pg_catalog."default" NOT NULL,
    reparo: bool = Column("td01_reparo",Boolean) #td01_reparo boolean,
    autoconfrede: bool = Column("td01_autoconfrede",Boolean) #td01_autoconfrede boolean,
    burnin: bool = Column("td01_burnin",Boolean) # td01_burnin boolean,
    fechaos: str = Column("td01_fechaos",String) # td01_fechaos character varying(1) COLLATE pg_catalog."default" DEFAULT 0,
    obrpn: bool = Column("td01_obrpn",Boolean) # td01_obrpn boolean,
    tipoid: str = Column("td01_tipoid",String) # td01_tipoid character varying(8) COLLATE pg_catalog."default" DEFAULT 0,

class Defeito(Base):
    __tablename__ = "td01_defeito"
    id: int = Column("td01_defeito_id", Integer, primary_key=True, nullable=False)
    descricao: str = Column("td01_descricao", String, nullable=False)
    ean: str = Column("td01_ean", String)
    grupo_id: str = Column("td01_grupo", String)
    codigo_id: str = Column("td01_codigo", String)
    agrupar: str = Column("td01_agrupar", String)
    categoria: str = Column("td01_categoria", String, nullable=False, default="Geral")
    
class ProdDefeito(Base):
    __tablename__ = "td01_prod_defeito"
    id: int = Column("td01_prod_defeito_id",Integer, primary_key=True, nullable=False) 
    obs: str = Column("td01_analise", String) 
    acao: str = Column("td01_reparo",String)
    status_id: int = Column("td01_status",Integer)
    dt: datetime =  Column("td01_dt",DateTime, default=datetime.date)
    hr1: time = Column("td01_hr1",Time)
    serie: str = Column("td01_serie", String)
    hr: time = Column("td01_hr",Time)
    producao_id: int = Column("td01_producao_id", Integer)
    defeito_id: int = Column("td01_defeito_id", Integer)
    timestamp: time = Column("td01_timestamp", Time)
    bipagem: str = Column("td01_bipagem", String)
    grupo_defeito_id: int = Column("td01_grupo_defeito_id", Integer)
 
class Produto(Base):
    __tablename__ = 'ts01_produto'
    id: str = Column("ts01_codigo", String,  primary_key=True, nullable=False) 
    descricao: str = Column("ts01_descricao", String) 
    narrativa: str = Column("ts01_narrativa",String)
    unidade: str = Column("ts01_unidade",String)
    descricao_especifica: str = Column("ts01_desc_esp",String)
    grupo: str = Column("ts01_grupo",String)
    cod_barras: str = Column("ts01_cod_barras",String)
    tipo: str = Column("td01_tipo",String) 
    
class Post(Base):
    __tablename__ = 'posts'
    id =  Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content= Column(String, nullable=True)
    published = Column(Boolean, nullable=True, default=True)
    rate = Column(Integer, nullable=True)
    post_date = Column(DateTime, default=datetime.time, nullable=False)
    
class User(Base):
    __tablename__ = "users"
    id  = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, unique=True)
    hashed_password = Column(String, nullable=False)
    is_active  = Column(Boolean, default=True)
    items = relationship("Item")

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String)
    description = Column(String)
       
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="items")