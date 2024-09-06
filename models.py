from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Pais(Base):
    __tablename__ = 'pais'
    id_pais = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    sigla = Column(String, index=True)

class Confederacao(Base):
    __tablename__ = 'confederacao'
    id_confederacao = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    id_pais = Column(Integer, ForeignKey('pais.id_pais'))
    pais = relationship("Pais")

class Edicao(Base):
    __tablename__ = 'edicao'
    ano = Column(Integer, primary_key=True, index=True)
    cidade_sede = Column(String)
    id_pais = Column(Integer, ForeignKey('pais.id_pais'))
    pais = relationship("Pais")

# Defina os outros modelos conforme sua estrutura
