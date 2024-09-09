from sqlalchemy import Column, Integer, String, Enum, Date, ForeignKey
from sqlalchemy.orm import relationship
from models import Base

class Atleta(Base):
    __tablename__ = 'atleta'  # Use minúsculas para manter consistência com o nome das tabelas

    id_atleta = Column(Integer, primary_key=True, autoincrement=True)
    genero = Column(Enum('M', 'F'), nullable=False)
    data_nasc = Column(Date, nullable=False)
    nome = Column(String(100), nullable=False)
    id_confederacao = Column(Integer, ForeignKey('confederacao.id_confederacao'))


    # Relacionamentos
    confederacao = relationship("Confederacao", back_populates="atletas")