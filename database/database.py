from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Configuração do banco de dados
DATABASE_URL = 'mysql+mysqlconnector://root:grdm9977@localhost/OlimpiadasDB'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Função para obter uma nova sessão
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
