from sqlalchemy import Column, Integer, String, Enum, Date, ForeignKey
from sqlalchemy.orm import relationship
from . import Base
from .modalidade import Modalidade
from .confederacao import Confederacao

class Atleta(Base):
    __tablename__ = 'atleta'

    id_atleta = Column(Integer, primary_key=True, autoincrement=True)
    genero = Column(Enum('M', 'F'), nullable=False)
    data_nasc = Column(Date, nullable=False)
    nome = Column(String(100), nullable=False)
    id_confederacao = Column(Integer, ForeignKey('confederacao.id_confederacao'))
    id_modalidade = Column(Integer, ForeignKey('modalidade.id_modalidade'))

    # Relacionamentos
    confederacao = relationship("Confederacao", back_populates="atletas")
    modalidade = relationship("Modalidade", back_populates="atletas")
