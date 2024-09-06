# crud/modalidade.py
from sqlalchemy.orm import Session
from models import Modalidade

def criar_modalidade(db: Session, nome: str):
    db_modalidade = Modalidade(nome=nome)
    db.add(db_modalidade)
    db.commit()
    db.refresh(db_modalidade)
    return db_modalidade

def ler_modalidade(db: Session, id_modalidade: int):
    return db.query(Modalidade).filter(Modalidade.id_modalidade == id_modalidade).first()

def atualizar_modalidade(db: Session, id_modalidade: int, nome: str):
    db_modalidade = db.query(Modalidade).filter(Modalidade.id_modalidade == id_modalidade).first()
    if db_modalidade:
        db_modalidade.nome = nome
        db.commit()
        db.refresh(db_modalidade)
    return db_modalidade

def deletar_modalidade(db: Session, id_modalidade: int):
    db_modalidade = db.query(Modalidade).filter(Modalidade.id_modalidade == id_modalidade).first()
    if db_modalidade:
        db.delete(db_modalidade)
        db.commit()
    return db_modalidade
