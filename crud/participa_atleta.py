# crud/participa_atleta_crud.py
from sqlalchemy.orm import Session
from models import ParticipaAtleta

def criar_participa_atleta(db: Session, id_atleta: int, id_evento: int):
    db_participa_atleta = ParticipaAtleta(id_atleta=id_atleta, id_evento=id_evento)
    db.add(db_participa_atleta)
    db.commit()
    db.refresh(db_participa_atleta)
    return db_participa_atleta

def ler_participa_atleta(db: Session, id_atleta: int, id_evento: int):
    return db.query(ParticipaAtleta).filter(ParticipaAtleta.id_atleta == id_atleta, ParticipaAtleta.id_evento == id_evento).first()

def atualizar_participa_atleta(db: Session, id_atleta: int, id_evento: int):
    db_participa_atleta = db.query(ParticipaAtleta).filter(ParticipaAtleta.id_atleta == id_atleta, ParticipaAtleta.id_evento == id_evento).first()
    if db_participa_atleta:
        # Atualize conforme necessário
        db.commit()
        db.refresh(db_participa_atleta)
    return db_participa_atleta

def deletar_participa_atleta(db: Session, id_atleta: int, id_evento: int):
    db_participa_atleta = db.query(ParticipaAtleta).filter(ParticipaAtleta.id_atleta == id_atleta, ParticipaAtleta.id_evento == id_evento).first()
    if db_participa_atleta:
        db.delete(db_participa_atleta)
        db.commit()
    return db_participa_atleta
