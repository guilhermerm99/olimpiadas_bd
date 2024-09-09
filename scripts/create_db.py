import mysql.connector
from mysql.connector import Error

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',          # Substitua pelo seu usuário do MySQL
            password='grdm9977',  # Substitua pela sua senha do MySQL
        )
        if connection.is_connected():
            print("Conexão ao MySQL estabelecida com sucesso")
            return connection
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

def create_database():
    connection = get_db_connection()
    if connection is not None:
        cursor = connection.cursor()
        try:
            # Criação do banco de dados e seleção
            cursor.execute("CREATE DATABASE IF NOT EXISTS OlimpiadasDB;")
            cursor.execute("USE OlimpiadasDB;")
            connection.commit()  # Confirma a criação do banco de dados

            # Comandos SQL para criar tabelas
            create_tables_sql = """
            -- Excluir as tabelas, se existirem
            DROP TABLE IF EXISTS Atletas_Participantes;
            DROP TABLE IF EXISTS Historico;
            DROP TABLE IF EXISTS Medalha;
            DROP TABLE IF EXISTS Evento;
            DROP TABLE IF EXISTS Recorde;
            DROP TABLE IF EXISTS Atleta;
            DROP TABLE IF EXISTS Local;
            DROP TABLE IF EXISTS Modalidade;
            DROP TABLE IF EXISTS Edicao;
            DROP TABLE IF EXISTS Confederacao;
            DROP TABLE IF EXISTS Pais;

            -- Criação da tabela País
            CREATE TABLE IF NOT EXISTS Pais (
                id_pais INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                sigla VARCHAR(3) NOT NULL,
                bandeira BLOB -- Dado binário para a bandeira
            );

            -- Criação da tabela Confederação
            CREATE TABLE IF NOT EXISTS Confederacao (
                id_confederacao INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                id_pais INT,
                FOREIGN KEY (id_pais) REFERENCES Pais(id_pais)
            );

            -- Criação da tabela Edição
            CREATE TABLE IF NOT EXISTS Edicao (
                ano YEAR PRIMARY KEY,
                cidade_sede VARCHAR(100) NOT NULL,
                id_pais INT,
                FOREIGN KEY (id_pais) REFERENCES Pais(id_pais)
            );

            -- Criação da tabela Modalidade
            CREATE TABLE IF NOT EXISTS Modalidade (
                id_modalidade INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(100) NOT NULL
            );

            -- Criação da tabela Local
            CREATE TABLE IF NOT EXISTS Local (
                id_local INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                cidade VARCHAR(100) NOT NULL,
                capacidade INT
            );

            -- Criação da tabela Atleta
            CREATE TABLE IF NOT EXISTS Atleta (
                id_atleta INT AUTO_INCREMENT PRIMARY KEY,
                genero ENUM('M', 'F') NOT NULL,
                data_nasc DATE NOT NULL,
                nome VARCHAR(100) NOT NULL,
                id_confederacao INT,
                id_modalidade INT,
                FOREIGN KEY (id_confederacao) REFERENCES Confederacao(id_confederacao),
                FOREIGN KEY (id_modalidade) REFERENCES Modalidade(id_modalidade)
            );

            -- Criação da tabela Recorde
            CREATE TABLE IF NOT EXISTS Recorde (
                id_recorde INT AUTO_INCREMENT PRIMARY KEY,
                tipo_marca VARCHAR(50),
                marca VARCHAR(50),
                id_atleta INT,
                tipo VARCHAR(50),
                FOREIGN KEY (id_atleta) REFERENCES Atleta(id_atleta)
            );

            -- Criação da tabela Evento
            CREATE TABLE IF NOT EXISTS Evento (
                id_evento INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                data DATE NOT NULL,
                tipo_numero VARCHAR(50),
                tipo_genero ENUM('M', 'F', 'Misto') NOT NULL,
                id_modalidade INT,
                id_recorde INT,
                id_local INT,
                FOREIGN KEY (id_modalidade) REFERENCES Modalidade(id_modalidade),
                FOREIGN KEY (id_recorde) REFERENCES Recorde(id_recorde),
                FOREIGN KEY (id_local) REFERENCES Local(id_local)
            );

            -- Criação da tabela Medalha
            CREATE TABLE IF NOT EXISTS Medalha (
                id_medalha INT AUTO_INCREMENT PRIMARY KEY,
                tipo ENUM('Ouro', 'Prata', 'Bronze') NOT NULL,
                id_atleta INT,
                id_evento INT,
                id_edicao YEAR,
                FOREIGN KEY (id_atleta) REFERENCES Atleta(id_atleta),
                FOREIGN KEY (id_evento) REFERENCES Evento(id_evento),
                FOREIGN KEY (id_edicao) REFERENCES Edicao(ano)
            );

            -- Criação da tabela Histórico
            CREATE TABLE IF NOT EXISTS Historico (
                id_historico INT AUTO_INCREMENT PRIMARY KEY,
                desempenho VARCHAR(255),
                id_atleta INT,
                id_evento INT,
                FOREIGN KEY (id_atleta) REFERENCES Atleta(id_atleta),
                FOREIGN KEY (id_evento) REFERENCES Evento(id_evento)
            );

            -- Criação da tabela Atletas_Participantes
            CREATE TABLE IF NOT EXISTS Atletas_Participantes (
                id_equipe INT,
                id_atleta INT,
                id_evento INT,
                PRIMARY KEY (id_equipe, id_atleta, id_evento),
                FOREIGN KEY (id_atleta) REFERENCES Atleta(id_atleta),
                FOREIGN KEY (id_evento) REFERENCES Evento(id_evento)
            );
            """

            # Execute commands one by one
            for statement in create_tables_sql.split(';'):
                statement = statement.strip()
                if statement:
                    cursor.execute(statement)
            
            connection.commit()  # Confirma a criação das tabelas
            print("Banco de dados e tabelas criados com sucesso.")
        except Error as e:
            print(f"Erro ao criar banco de dados ou tabelas: {e}")
        finally:
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
