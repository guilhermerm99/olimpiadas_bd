# crud/medalha_crud.py
from sqlalchemy.orm import Session
from models import Medalha

def criar_medalha(db: Session, tipo: str, descricao: str):
    db_medalha = Medalha(tipo=tipo, descricao=descricao)
    db.add(db_medalha)
    db.commit()
    db.refresh(db_medalha)
    return db_medalha

def ler_medalha(db: Session, medalha_id: int):
    return db.query(Medalha).filter(Medalha.id_medalha == medalha_id).first()

def atualizar_medalha(db: Session, medalha_id: int, tipo: str, descricao: str):
    db_medalha = db.query(Medalha).filter(Medalha.id_medalha == medalha_id).first()
    if db_medalha:
        db_medalha.tipo = tipo
        db_medalha.descricao = descricao
        db.commit()
        db.refresh(db_medalha)
    return db_medalha

def deletar_medalha(db: Session, medalha_id: int):
    db_medalha = db.query(Medalha).filter(Medalha.id_medalha == medalha_id).first()
    if db_medalha:
        db.delete(db_medalha)
        db.commit()
    return db_medalha
