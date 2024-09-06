# crud/confederacao.py
from sqlalchemy.orm import Session
from models import Confederacao

def criar_confederacao(db: Session, nome: str, id_pais: int):
    db_confederacao = Confederacao(nome=nome, id_pais=id_pais)
    db.add(db_confederacao)
    db.commit()
    db.refresh(db_confederacao)
    return db_confederacao

def ler_confederacao(db: Session, id_confederacao: int):
    return db.query(Confederacao).filter(Confederacao.id_confederacao == id_confederacao).first()

def atualizar_confederacao(db: Session, id_confederacao: int, nome: str, id_pais: int):
    db_confederacao = db.query(Confederacao).filter(Confederacao.id_confederacao == id_confederacao).first()
    if db_confederacao:
        db_confederacao.nome = nome
        db_confederacao.id_pais = id_pais
        db.commit()
        db.refresh(db_confederacao)
    return db_confederacao

def deletar_confederacao(db: Session, id_confederacao: int):
    db_confederacao = db.query(Confederacao).filter(Confederacao.id_confederacao == id_confederacao).first()
    if db_confederacao:
        db.delete(db_confederacao)
        db.commit()
    return db_confederacao
