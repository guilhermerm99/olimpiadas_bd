# crud/historico_crud.py
from sqlalchemy.orm import Session
from models import Historico

def criar_historico(db: Session, data: str, evento: str, resultado: str):
    db_historico = Historico(data=data, evento=evento, resultado=resultado)
    db.add(db_historico)
    db.commit()
    db.refresh(db_historico)
    return db_historico

def ler_historico(db: Session, historico_id: int):
    return db.query(Historico).filter(Historico.id_historico == historico_id).first()

def atualizar_historico(db: Session, historico_id: int, data: str, evento: str, resultado: str):
    db_historico = db.query(Historico).filter(Historico.id_historico == historico_id).first()
    if db_historico:
        db_historico.data = data
        db_historico.evento = evento
        db_historico.resultado = resultado
        db.commit()
        db.refresh(db_historico)
    return db_historico

def deletar_historico(db: Session, historico_id: int):
    db_historico = db.query(Historico).filter(Historico.id_historico == historico_id).first()
    if db_historico:
        db.delete(db_historico)
        db.commit()
    return db_historico
