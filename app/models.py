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
    local_id: str = Column("td01_id",String, ForeignKey("locais.id"))
    dt: datetime =  Column("td01_dt",DateTime, default=datetime.date)
    hr: time = Column("td01_hr",Time)
    serie: int = Column("td01_serie",Integer)
    user_id: int = Column("td01_re",Integer, ForeignKey("users.id"))
    setor_id: str = Column("td01_local",String, ForeignKey("setors.id"))
    os_id: int = Column("td01_os",Integer, ForeignKey("oss.id"))

class Setor(Base):
    __tablename__ = "td01_identificador"
    id: int = Column("td01_id",String, primary_key=True, nullable=False) #td01_id character varying(6) COLLATE pg_catalog."default" NOT NULL,
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