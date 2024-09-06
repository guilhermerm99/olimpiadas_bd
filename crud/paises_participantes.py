# crud/paises_participantes.py
from sqlalchemy.orm import Session
from models import PaisesParticipantes

def criar_paises_participantes(db: Session, ano: int, id_confederacao: int):
    db_paises_participantes = PaisesParticipantes(ano=ano, id_confederacao=id_confederacao)
    db.add(db_paises_participantes)
    db.commit()
    db.refresh(db_paises_participantes)
    return db_paises_participantes

def ler_paises_participantes(db: Session, ano: int, id_confederacao: int):
    return db.query(PaisesParticipantes).filter(PaisesParticipantes.ano == ano, PaisesParticipantes.id_confederacao == id_confederacao).first()

def atualizar_paises_participantes(db: Session, ano: int, id_confederacao: int):
    db_paises_participantes = db.query(PaisesParticipantes).filter(PaisesParticipantes.ano == ano, PaisesParticipantes.id_confederacao == id_confederacao).first()
    if db_paises_participantes:
        # Atualize conforme necessário
        db.commit()
        db.refresh(db_paises_participantes)
    return db_paises_participantes

def deletar_paises_participantes(db: Session, ano: int, id_confederacao: int):
    db_paises_participantes = db.query(PaisesParticipantes).filter(PaisesParticipantes.ano == ano, PaisesParticipantes.id_confederacao == id_confederacao).first()
    if db_paises_participantes:
        db.delete(db_paises_participantes)
        db.commit()
    return db_paises_participantes
