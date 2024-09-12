from sqlalchemy import Column, Integer, String, LargeBinary
from sqlalchemy.orm import relationship
from models import Base

class Pais(Base):
    __tablename__ = 'pais'
    
    id_pais = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False, unique=True)
    sigla = Column(String, nullable=False)
    bandeira = Column(LargeBinary, nullable=True)
    
    # Relacionamento com Confederacao
    confederacoes = relationship("Confederacao", back_populates="pais")