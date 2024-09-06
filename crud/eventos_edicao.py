# crud/eventos_edição_crud.py
from sqlalchemy.orm import Session
from models import EventosEdicao

def criar_eventos_edicao(db: Session, id_evento: int, ano: int):
    db_eventos_edicao = EventosEdicao(id_evento=id_evento, ano=ano)
    db.add(db_eventos_edicao)
    db.commit()
    db.refresh(db_eventos_edicao)
    return db_eventos_edicao

def ler_eventos_edicao(db: Session, id_evento: int, ano: int):
    return db.query(EventosEdicao).filter(EventosEdicao.id_evento == id_evento, EventosEdicao.ano == ano).first()

def atualizar_eventos_edicao(db: Session, id_evento: int, ano: int):
    db_eventos_edicao = db.query(EventosEdicao).filter(EventosEdicao.id_evento == id_evento, EventosEdicao.ano == ano).first()
    if db_eventos_edicao:
        # Atualize conforme necessário
        db.commit()
        db.refresh(db_eventos_edicao)
    return db_eventos_edicao

def deletar_eventos_edicao(db: Session, id_evento: int, ano: int):
    db_eventos_edicao = db.query(EventosEdicao).filter(EventosEdicao.id_evento == id_evento, EventosEdicao.ano == ano).first()
    if db_eventos_edicao:
        db.delete(db_eventos_edicao)
        db.commit()
    return db_eventos_edicao
