# crud/atleta2.py
from sqlalchemy.orm import Session
from models import Atleta2

def criar_atleta2(db: Session, id_atleta: int, id_evento: int):
    db_atleta2 = Atleta2(id_atleta=id_atleta, id_evento=id_evento)
    db.add(db_atleta2)
    db.commit()
    db.refresh(db_atleta2)
    return db_atleta2

def ler_atleta2(db: Session, id_atleta: int, id_evento: int):
    return db.query(Atleta2).filter(Atleta2.id_atleta == id_atleta, Atleta2.id_evento == id_evento).first()

def atualizar_atleta2(db: Session, id_atleta: int, id_evento: int):
    db_atleta2 = db.query(Atleta2).filter(Atleta2.id_atleta == id_atleta, Atleta2.id_evento == id_evento).first()
    if db_atleta2:
        # Atualize conforme necessário
        db.commit()
        db.refresh(db_atleta2)
    return db_atleta2

def deletar_atleta2(db: Session, id_atleta: int, id_evento: int):
    db_atleta2 = db.query(Atleta2).filter(Atleta2.id_atleta == id_atleta, Atleta2.id_evento == id_evento).first()
    if db_atleta2:
        db.delete(db_atleta2)
        db.commit()
    return db_atleta2
