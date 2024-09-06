from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Pais, Confederacao, Edicao, Modalidade, Evento, Equipe, Atleta, Recorde, Medalha, Historico, EventosEdicao, ParticipaAtleta, Atleta1, Atleta2, EdicaoMedalha, PaisesParticipantes
import config

# Configuração do banco de dados
engine = create_engine(config.DATABASE_URL, echo=True)

# Criar todas as tabelas no banco de dados
Base.metadata.create_all(engine)

# Criar uma sessão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

def create_pais(nome: str, sigla: str):
    new_pais = Pais(nome=nome, sigla=sigla)
    session.add(new_pais)
    session.commit()

def get_pais(id_pais: int):
    return session.query(Pais).filter(Pais.id_pais == id_pais).first()

def update_pais(id_pais: int, nome: str, sigla: str):
    pais = session.query(Pais).filter(Pais.id_pais == id_pais).first()
    if pais:
        pais.nome = nome
        pais.sigla = sigla
        session.commit()

def delete_pais(id_pais: int):
    pais = session.query(Pais).filter(Pais.id_pais == id_pais).first()
    if pais:
        session.delete(pais)
        session.commit()

# Exemplo de uso das funções CRUD
if __name__ == "__main__":
    # Criar um novo país
    create_pais("Brasil", "BR")

    # Obter e exibir um país
    pais = get_pais(1)
    if pais:
        print(f"ID: {pais.id_pais}, Nome: {pais.nome}, Sigla: {pais.sigla}")

    # Atualizar um país
    update_pais(1, "Brasil Atualizado", "BRA")

    # Deletar um país
    delete_pais(1)

    # Fechar a sessão
    session.close()
