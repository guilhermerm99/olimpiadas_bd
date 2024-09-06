from sqlalchemy.orm import Session
from models import ParticipaMedalha

def criar_participa_medalha(db: Session, id_medalha: int, id_evento: int, id_atleta: int):
    db_participa_medalha = ParticipaMedalha(id_medalha=id_medalha, id_evento=id_evento, id_atleta=id_atleta)
    db.add(db_participa_medalha)
    db.commit()
    db.refresh(db_participa_medalha)
    return db_participa_medalha

def ler_participa_medalha(db: Session, id_medalha: int, id_evento: int, id_atleta: int):
    return db.query(ParticipaMedalha).filter(ParticipaMedalha.id_medalha == id_medalha, ParticipaMedalha.id_evento == id_evento, ParticipaMedalha.id_atleta == id_atleta).first()

def atualizar_participa_medalha(db: Session, id_medalha: int, id_evento: int, id_atleta: int):
    db_participa_medalha = db.query(ParticipaMedalha).filter(ParticipaMedalha.id_medalha == id_medalha, ParticipaMedalha.id_evento == id_evento, ParticipaMedalha.id_atleta == id_atleta).first()
    if db_participa_medalha:
        # Atualize conforme necessário
        db.commit()
        db.refresh(db_participa_medalha)
    return db_participa_medalha

def deletar_participa_medalha(db: Session, id_medalha: int, id_evento: int, id_atleta: int):
    db_participa_medalha = db.query(ParticipaMedalha).filter(ParticipaMedalha.id_medalha == id_medalha, ParticipaMedalha.id_evento == id_evento, ParticipaMedalha.id_atleta == id_atleta).first()
    if db_participa_medalha:
        db.delete(db_participa_medalha)
        db.commit()
    return db_participa_medalha
