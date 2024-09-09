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
def test_pais_exclusao():
    session = SessionLocal()
    try:
        # ID do país a ser removido
        id_pais = 8

        # Remove o país com o ID especificado
        pais_para_remover = session.query(Pais).filter(Pais.id_pais == id_pais).first()
        if pais_para_remover:
            session.delete(pais_para_remover)
            session.commit()
            print(f"Pais com ID {id_pais} removido.")
        else:
            print(f"Nenhum país encontrado com ID {id_pais}.")

    except Exception as e:
        print(f"Erro ao remover pais: {e}")
    finally:
        session.close()

# Executa o teste
test_pais_exclusao()
