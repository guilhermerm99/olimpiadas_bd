# crud/atleta1.py
from sqlalchemy.orm import Session
from models import Atleta1

def criar_atleta1(db: Session, id_atleta: int, id_evento: int):
    db_atleta1 = Atleta1(id_atleta=id_atleta, id_evento=id_evento)
    db.add(db_atleta1)
    db.commit()
    db.refresh(db_atleta1)
    return db_atleta1

def ler_atleta1(db: Session, id_atleta: int, id_evento: int):
    return db.query(Atleta1).filter(Atleta1.id_atleta == id_atleta, Atleta1.id_evento == id_evento).first()

def atualizar_atleta1(db: Session, id_atleta: int, id_evento: int):
    db_atleta1 = db.query(Atleta1).filter(Atleta1.id_atleta == id_atleta, Atleta1.id_evento == id_evento).first()
    if db_atleta1:
        # Atualize conforme necessário
        db.commit()
        db.refresh(db_atleta1)
    return db_atleta1

def deletar_atleta1(db: Session, id_atleta: int, id_evento: int):
    db_atleta1 = db.query(Atleta1).filter(Atleta1.id_atleta == id_atleta, Atleta1.id_evento == id_evento).first()
    if db_atleta1:
        db.delete(db_atleta1)
        db.commit()
    return db_atleta1
