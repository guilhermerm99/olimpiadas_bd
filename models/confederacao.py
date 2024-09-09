from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models import Base

class Confederacao(Base):
    __tablename__ = 'confederacao'
    
    id_confederacao = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    
    # Relacionamento com Pais
    id_pais = Column(Integer, ForeignKey('pais.id_pais'))
    pais = relationship("Pais", back_populates="confederacoes")
    
    # Relacionamento com Atleta
    atletas = relationship("Atleta", back_populates="confederacao")
