# crud/edicao.py
from sqlalchemy.orm import Session
from models import Edicao

def criar_edicao(db: Session, ano: int, cidade_sede: str, id_pais: int):
    db_edicao = Edicao(ano=ano, cidade_sede=cidade_sede, id_pais=id_pais)
    db.add(db_edicao)
    db.commit()
    db.refresh(db_edicao)
    return db_edicao

def ler_edicao(db: Session, ano: int):
    return db.query(Edicao).filter(Edicao.ano == ano).first()

def atualizar_edicao(db: Session, ano: int, cidade_sede: str, id_pais: int):
    db_edicao = db.query(Edicao).filter(Edicao.ano == ano).first()
    if db_edicao:
        db_edicao.cidade_sede = cidade_sede
        db_edicao.id_pais = id_pais
        db.commit()
        db.refresh(db_edicao)
    return db_edicao

def deletar_edicao(db: Session, ano: int):
    db_edicao = db.query(Edicao).filter(Edicao.ano == ano).first()
    if db_edicao:
        db.delete(db_edicao)
        db.commit()
    return db_edicao
