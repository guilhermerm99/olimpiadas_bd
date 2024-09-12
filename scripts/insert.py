import mysql.connector
from mysql.connector import Error

def connect_to_mysql():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='grdm9977',
            database='olimpiadasdb'
        )
        if connection.is_connected():
            print("Conexão ao MySQL estabelecida com sucesso")
            return connection
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

def execute_query(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Consulta executada e transação confirmada")
    except mysql.connector.Error as err:
        print(f"Erro ao executar a consulta: {err}")
    finally:
        cursor.close()

def insert_data():
    connection = connect_to_mysql()
    if connection is None:
        return

    try:
        # Limpeza de dados existentes
        limpar_dados_sql = """
        DELETE FROM Atletas_Participantes;
        DELETE FROM Medalha;
        DELETE FROM Historico;
        DELETE FROM Evento;
        DELETE FROM Recorde;
        DELETE FROM Atleta;
        DELETE FROM Local;
        DELETE FROM Modalidade;
        DELETE FROM Edicao;
        DELETE FROM Confederacao;
        DELETE FROM Pais;
        """
        for query in limpar_dados_sql.split(';'):
            query = query.strip()
            if query:
                execute_query(connection, query)
        
        # Inserções
        pais_sql = """
        INSERT IGNORE INTO Pais (nome, sigla, bandeira) VALUES 
        ('Brasil', 'BRA', NULL),
        ('Estados Unidos', 'USA', NULL),
        ('Jamaica', 'JAM', NULL),
        ('China', 'CHN', NULL),
        ('França', 'FRA', NULL),
        ('Japão', 'JPN', NULL),
        ('Inglaterra', 'ENG', NULL);
        """
        execute_query(connection, pais_sql)
        
        confederacao_sql = """
        INSERT IGNORE INTO Confederacao (nome, id_pais) VALUES
        ('Comitê Olímpico do Brasil', 1),
        ('Comitê Olímpico e Paralímpico dos Estados Unidos', 2),
        ('Comitê Olímpico da Jamaica', 3),
        ('Comitê Olímpico da China', 4),
        ('Comitê Olímpico e Esportivo da França', 5),
        ('Comitê Olímpico do Japão', 6),
        ('Comitê Olímpico da Grã-Bretanha', 7);
        """
        execute_query(connection, confederacao_sql)
        
        edicao_sql = """
        INSERT IGNORE INTO Edicao (ano, cidade_sede, id_pais) VALUES
        (2016, 'Rio de Janeiro', 1),
        (2020, 'Tóquio', 6),
        (2012, 'Londres', 7),
        (2008, 'Pequim', 4),
        (2024, 'Paris', 5);
        """
        execute_query(connection, edicao_sql)
        
        modalidade_sql = """
        INSERT IGNORE INTO Modalidade (nome) VALUES
        ('Atletismo'),
        ('Natação'),
        ('Ginástica'),
        ('Judô'),
        ('Vôlei'),
        ('Skate');
        """
        execute_query(connection, modalidade_sql)
        
        local_sql = """
        INSERT IGNORE INTO Local (nome, cidade, capacidade) VALUES
        ('Estádio Olímpico Nilton Santos', 'Rio de Janeiro', 70000),
        ('Estádio Nacional do Japão', 'Tóquio', 68000),
        ('The O2 Arena', 'Londres', 20000),
        ('Estádio Olímpico de Londres', 'Londres', 62500),
        ('Farmasi Arena', 'Rio de Janeiro', 18000);
        """
        execute_query(connection, local_sql)
        
        atleta_sql = """
        INSERT IGNORE INTO Atleta (genero, data_nasc, nome, id_confederacao, id_modalidade) VALUES
        ('M', '1986-08-21', 'Usain Bolt', 3, 1),
        ('F', '1985-11-18', 'Allyson Felix', 2, 1),
        ('M', '1992-12-18', 'Ryan Crouser', 2, 1),
        ('M', '1990-04-16', 'Arthur Zanetti', 1, 3),
        ('F', '1997-03-14', 'Simone Biles', 2, 3);
        """
        execute_query(connection, atleta_sql)
        
        recorde_sql = """
        INSERT IGNORE INTO Recorde (tipo_marca, marca, id_atleta, tipo) VALUES
        ('Tempo', '9.58s', 1, 'Mundial'),
        ('Tempo', '21.69s', 2, 'Olimpico'),
        ('Distância', '23.56m', 3, 'Mundial'),
        ('Pontuação', '16.050', 4, 'Olimpico'),
        ('Pontuação', '15.333', 5, 'Mundial');
        """
        execute_query(connection, recorde_sql)
        
        evento_sql = """
        INSERT IGNORE INTO Evento (nome, data, tipo_numero, tipo_genero, id_modalidade, id_recorde, id_local) VALUES
        ('100 metros rasos masculino', '2016-08-14', 'Individual', 'M', 1, 1, 1),
        ('200 metros rasos feminino', '2016-08-17', 'Individual', 'F', 1, 2, 4),
        ('Arremesso de peso masculino', '2020-08-05', 'Individual', 'M', 1, 3, 2),
        ('Argolas masculino', '2012-08-06', 'Individual', 'M', 3, 4, 5),
        ('Solo feminino', '2016-08-16', 'Individual', 'F', 3, 5, 5);
        """
        execute_query(connection, evento_sql)
        
        medalha_sql = """
        INSERT IGNORE INTO Medalha (tipo, id_atleta, id_evento, id_edicao) VALUES
        ('Ouro', 1, 1, 2016),
        ('Ouro', 2, 2, 2012),
        ('Ouro', 3, 3, 2020),
        ('Ouro', 4, 4, 2016),
        ('Ouro', 5, 5, 2020);
        """
        execute_query(connection, medalha_sql)
        
        historico_sql = """
        INSERT IGNORE INTO Historico (desempenho, id_atleta, id_evento) VALUES
        ('1º lugar, recorde mundial', 1, 1),
        ('1º lugar', 2, 2),
        ('1º lugar, recorde olímpico', 3, 3),
        ('1º lugar', 4, 4),
        ('1º lugar', 5, 5);
        """
        execute_query(connection, historico_sql)
        
        atletas_participantes_sql = """
        INSERT IGNORE INTO Atletas_Participantes (id_equipe, id_atleta, id_evento) VALUES
        (1, 1, 1),
        (2, 2, 2),
        (3, 3, 3),
        (4, 4, 4),
        (5, 5, 5);
        """
        execute_query(connection, atletas_participantes_sql)

    except mysql.connector.Error as err:
        print(f"Erro ao executar a consulta: {err}")
    finally:
        if connection.is_connected():
            connection.close()
            print("Conexão ao MySQL encerrada")

if __name__ == "__main__":
    insert_data()
