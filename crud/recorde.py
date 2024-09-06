# crud/recorde_crud.py
from sqlalchemy.orm import Session
from models import Recorde

def criar_recorde(db: Session, valor: float, unidade: str):
    db_recorde = Recorde(valor=valor, unidade=unidade)
    db.add(db_recorde)
    db.commit()
    db.refresh(db_recorde)
    return db_recorde

def ler_recorde(db: Session, recorde_id: int):
    return db.query(Recorde).filter(Recorde.id_recorde == recorde_id).first()

def atualizar_recorde(db: Session, recorde_id: int, valor: float, unidade: str):
    db_recorde = db.query(Recorde).filter(Recorde.id_recorde == recorde_id).first()
    if db_recorde:
        db_recorde.valor = valor
        db_recorde.unidade = unidade
        db.commit()
        db.refresh(db_recorde)
    return db_recorde

def deletar_recorde(db: Session, recorde_id: int):
    db_recorde = db.query(Recorde).filter(Recorde.id_recorde == recorde_id).first()
    if db_recorde:
        db.delete(db_recorde)
        db.commit()
    return db_recorde
