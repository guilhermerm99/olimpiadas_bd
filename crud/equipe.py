# crud/equipe_crud.py
from sqlalchemy.orm import Session
from models import Equipe

def criar_equipe(db: Session, nome: str, idConfederacao: int, idEvento: int):
    db_equipe = Equipe(nome=nome, idConfederacao=idConfederacao, idEvento=idEvento)
    db.add(db_equipe)
    db.commit()
    db.refresh(db_equipe)
    return db_equipe

def ler_equipe(db: Session, equipe_id: int):
    return db.query(Equipe).filter(Equipe.id_equipe == equipe_id).first()

def atualizar_equipe(db: Session, equipe_id: int, nome: str, idConfederacao: int, idEvento: int):
    db_equipe = db.query(Equipe).filter(Equipe.id_equipe == equipe_id).first()
    if db_equipe:
        db_equipe.nome = nome
        db_equipe.idConfederacao = idConfederacao
        db_equipe.idEvento = idEvento
        db.commit()
        db.refresh(db_equipe)
    return db_equipe

def deletar_equipe(db: Session, equipe_id: int):
    db_equipe = db.query(Equipe).filter(Equipe.id_equipe == equipe_id).first()
    if db_equipe:
        db.delete(db_equipe)
        db.commit()
    return db_equipe
