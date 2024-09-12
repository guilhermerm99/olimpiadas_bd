from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Pais

# Configuração do banco de dados
DATABASE_URL = "mysql+mysqlconnector://root:grdm9977@localhost/OlimpiadasDB"  # Use o URL apropriado para o seu banco de dados
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Criação das tabelas
Base.metadata.create_all(bind=engine)

# Função de teste
def test_pais_insercao():
    session = SessionLocal()
    try:
        # Lê o arquivo da bandeira como binário
        with open(r'C:\Users\guilherme\Documents\olimpiadas_bd\static\bandeiras\br.svg', "rb") as f:
            bandeira_bin = f.read()
        
        novo_pais = Pais(nome="Brasil", sigla="BR", bandeira=bandeira_bin)
        session.add(novo_pais)
        session.commit()
        print("Pais inserido com sucesso!")
    except Exception as e:
        print(f"Erro ao inserir pais: {e}")
    finally:
        session.close()

# Executa o teste
test_pais_insercao()
