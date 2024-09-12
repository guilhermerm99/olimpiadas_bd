from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base

class Modalidade(Base):
    __tablename__ = 'modalidade'

    id_modalidade = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)

    # Relacionamento com Atleta
    atletas = relationship("Atleta", back_populates="modalidade")
