# crud/atleta_crud.py
from sqlalchemy.orm import Session
from models import Atleta

def criar_atleta(db: Session, genero: str, data_nasc: str, nome: str, idConfederacao: int, idModalidade: int, idEquipe: int):
    db_atleta = Atleta(genero=genero, data_nasc=data_nasc, nome=nome, idConfederacao=idConfederacao, idModalidade=idModalidade, idEquipe=idEquipe)
    db.add(db_atleta)
    db.commit()
    db.refresh(db_atleta)
    return db_atleta

def ler_atleta(db: Session, atleta_id: int):
    return db.query(Atleta).filter(Atleta.id_atleta == atleta_id).first()

def atualizar_atleta(db: Session, atleta_id: int, genero: str, data_nasc: str, nome: str, idConfederacao: int, idModalidade: int, idEquipe: int):
    db_atleta = db.query(Atleta).filter(Atleta.id_atleta == atleta_id).first()
    if db_atleta:
        db_atleta.genero = genero
        db_atleta.data_nasc = data_nasc
        db_atleta.nome = nome
        db_atleta.idConfederacao = idConfederacao
        db_atleta.idModalidade = idModalidade
        db_atleta.idEquipe = idEquipe
        db.commit()
        db.refresh(db_atleta)
    return db_atleta

def deletar_atleta(db: Session, atleta_id: int):
    db_atleta = db.query(Atleta).filter(Atleta.id_atleta == atleta_id).first()
    if db_atleta:
        db.delete(db_atleta)
        db.commit()
    return db_atleta
