# crud/edicao_medalha.py
from sqlalchemy.orm import Session
from models import EdicaoMedalha

def criar_edicao_medalha(db: Session, id_medalha: int, ano: int):
    db_edicao_medalha = EdicaoMedalha(id_medalha=id_medalha, ano=ano)
    db.add(db_edicao_medalha)
    db.commit()
    db.refresh(db_edicao_medalha)
    return db_edicao_medalha

def ler_edicao_medalha(db: Session, id_medalha: int, ano: int):
    return db.query(EdicaoMedalha).filter(EdicaoMedalha.id_medalha == id_medalha, EdicaoMedalha.ano == ano).first()

def atualizar_edicao_medalha(db: Session, id_medalha: int, ano: int):
    db_edicao_medalha = db.query(EdicaoMedalha).filter(EdicaoMedalha.id_medalha == id_medalha, EdicaoMedalha.ano == ano).first()
    if db_edicao_medalha:
        # Atualize conforme necessário
        db.commit()
        db.refresh(db_edicao_medalha)
    return db_edicao_medalha

def deletar_edicao_medalha(db: Session, id_medalha: int, ano: int):
    db_edicao_medalha = db.query(EdicaoMedalha).filter(EdicaoMedalha.id_medalha == id_medalha, EdicaoMedalha.ano == ano).first()
    if db_edicao_medalha:
        db.delete(db_edicao_medalha)
        db.commit()
    return db_edicao_medalha
