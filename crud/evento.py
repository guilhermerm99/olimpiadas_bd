# crud/evento.py
from sqlalchemy.orm import Session
from models import Evento

def criar_evento(db: Session, nome: str, data: str, tipo_numero: str, tipo_genero: str, id_modalidade: int, id_recorde: int):
    db_evento = Evento(nome=nome, data=data, tipo_numero=tipo_numero, tipo_genero=tipo_genero, id_modalidade=id_modalidade, id_recorde=id_recorde)
    db.add(db_evento)
    db.commit()
    db.refresh(db_evento)
    return db_evento

def ler_evento(db: Session, id_evento: int):
    return db.query(Evento).filter(Evento.id_evento == id_evento).first()

def atualizar_evento(db: Session, id_evento: int, nome: str, data: str, tipo_numero: str, tipo_genero: str, id_modalidade: int, id_recorde: int):
    db_evento = db.query(Evento).filter(Evento.id_evento == id_evento).first()
    if db_evento:
        db_evento.nome = nome
        db_evento.data = data
        db_evento.tipo_numero = tipo_numero
        db_evento.tipo_genero = tipo_genero
        db_evento.id_modalidade = id_modalidade
        db_evento.id_recorde = id_recorde
        db.commit()
        db.refresh(db_evento)
    return db_evento

def deletar_evento(db: Session, id_evento: int):
    db_evento = db.query(Evento).filter(Evento.id_evento == id_evento).first()
    if db_evento:
        db.delete(db_evento)
        db.commit()
    return db_evento
