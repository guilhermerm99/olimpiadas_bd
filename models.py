from sqlalchemy import (
    Column, Integer, String, Date, SmallInteger, ForeignKey, CheckConstraint, CHAR
)

from sqlalchemy.orm import Session
from models import SuaClasseModel

from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Pais(Base):
    __tablename__ = 'pais'

    id_pais = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    sigla = Column(CHAR(3), nullable=False)


class Confederacao(Base):
    __tablename__ = 'confederacao'

    id_confederacao = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    id_pais = Column(Integer, ForeignKey('pais.id_pais'))


class Edicao(Base):
    __tablename__ = 'edicao'

    ano = Column(SmallInteger, primary_key=True)
    cidade_sede = Column(String(100), nullable=False)
    id_pais = Column(Integer, ForeignKey('pais.id_pais'))

    __table_args__ = (
        CheckConstraint('ano BETWEEN 1000 AND 9999', name='ano_valid_range'),
    )


class Modalidade(Base):
    __tablename__ = 'modalidade'

    id_modalidade = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)


class Evento(Base):
    __tablename__ = 'evento'

    id_evento = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    data = Column(Date, nullable=False)
    tipo_numero = Column(String(20), nullable=False)
    tipo_genero = Column(String(20), nullable=False)
    id_modalidade = Column(Integer, ForeignKey('modalidade.id_modalidade'))
    id_recorde = Column(Integer)  # Foreign key for recorde, needs to be linked once recorde is created


class Equipe(Base):
    __tablename__ = 'equipe'

    id_equipe = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    id_confederacao = Column(Integer, ForeignKey('confederacao.id_confederacao'))
    id_evento = Column(Integer, ForeignKey('evento.id_evento'))


class Atleta(Base):
    __tablename__ = 'atleta'

    id_atleta = Column(Integer, primary_key=True, autoincrement=True)
    genero = Column(CHAR(1), nullable=False)
    data_nasc = Column(Date, nullable=False)
    nome = Column(String(100), nullable=False)
    id_confederacao = Column(Integer, ForeignKey('confederacao.id_confederacao'))
    id_modalidade = Column(Integer, ForeignKey('modalidade.id_modalidade'))
    id_equipe = Column(Integer, ForeignKey('equipe.id_equipe'))


class Recorde(Base):
    __tablename__ = 'recorde'

    id_recorde = Column(Integer, primary_key=True, autoincrement=True)
    descricao = Column(String(255), nullable=False)


class Medalha(Base):
    __tablename__ = 'medalha'

    id_medalha = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(String(20), nullable=False)
    id_atleta = Column(Integer, ForeignKey('atleta.id_atleta'))
    id_equipe = Column(Integer, ForeignKey('equipe.id_equipe'))
    id_evento = Column(Integer, ForeignKey('evento.id_evento'))


class Historico(Base):
    __tablename__ = 'historico'

    id_historico = Column(Integer, primary_key=True, autoincrement=True)
    desempenho = Column(String(255), nullable=False)
    id_atleta = Column(Integer, ForeignKey('atleta.id_atleta'))
    id_equipe = Column(Integer, ForeignKey('equipe.id_equipe'))
    id_edicao = Column(SmallInteger, ForeignKey('edicao.ano'))

    __table_args__ = (
        CheckConstraint('id_edicao BETWEEN 1000 AND 9999', name='id_edicao_valid_range'),
    )


class EventosEdicao(Base):
    __tablename__ = 'eventos_edicao'

    id_evento = Column(Integer, ForeignKey('evento.id_evento'), primary_key=True)
    ano = Column(SmallInteger, ForeignKey('edicao.ano'), primary_key=True)

    __table_args__ = (
        CheckConstraint('ano BETWEEN 1000 AND 9999', name='ano_valid_range_eventos_edicao'),
    )


class ParticipaAtleta(Base):
    __tablename__ = 'participa_atleta'

    ano = Column(SmallInteger, ForeignKey('edicao.ano'), primary_key=True)
    id_atleta = Column(Integer, ForeignKey('atleta.id_atleta'), primary_key=True)

    __table_args__ = (
        CheckConstraint('ano BETWEEN 1000 AND 9999', name='ano_valid_range_participa_atleta'),
    )


class Atleta1(Base):
    __tablename__ = 'atleta1'

    id_atleta = Column(Integer, ForeignKey('atleta.id_atleta'), primary_key=True)
    id_evento = Column(Integer, ForeignKey('evento.id_evento'), primary_key=True)


class Atleta2(Base):
    __tablename__ = 'atleta2'

    id_atleta = Column(Integer, ForeignKey('atleta.id_atleta'), primary_key=True)
    id_evento = Column(Integer, ForeignKey('evento.id_evento'), primary_key=True)


class EdicaoMedalha(Base):
    __tablename__ = 'edicao_medalha'

    id_medalha = Column(Integer, ForeignKey('medalha.id_medalha'), primary_key=True)
    ano = Column(SmallInteger, ForeignKey('edicao.ano'), primary_key=True)

    __table_args__ = (
        CheckConstraint('ano BETWEEN 1000 AND 9999', name='ano_valid_range_edicao_medalha'),
    )


class PaisesParticipantes(Base):
    __tablename__ = 'paises_participantes'

    ano = Column(SmallInteger, ForeignKey('edicao.ano'), primary_key=True)
    id_confederacao = Column(Integer, ForeignKey('confederacao.id_confederacao'), primary_key=True)

    __table_args__ = (
        CheckConstraint('ano BETWEEN 1000 AND 9999', name='ano_valid_range_paises_participantes'),
    )