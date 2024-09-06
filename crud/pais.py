# crud/pais.py
from sqlalchemy.orm import Session
from models import Pais

def criar_pais(db: Session, nome: str, sigla: str):
    db_pais = Pais(nome=nome, sigla=sigla)
    db.add(db_pais)
    db.commit()
    db.refresh(db_pais)
    return db_pais

def ler_pais(db: Session, id_pais: int):
    return db.query(Pais).filter(Pais.id_pais == id_pais).first()

def atualizar_pais(db: Session, id_pais: int, nome: str, sigla: str):
    db_pais = db.query(Pais).filter(Pais.id_pais == id_pais).first()
    if db_pais:
        db_pais.nome = nome
        db_pais.sigla = sigla
        db.commit()
        db.refresh(db_pais)
    return db_pais

def deletar_pais(db: Session, id_pais: int):
    db_pais = db.query(Pais).filter(Pais.id_pais == id_pais).first()
    if db_pais:
        db.delete(db_pais)
        db.commit()
    return db_pais
