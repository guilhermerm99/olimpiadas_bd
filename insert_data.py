# executar assim: python seu_script.py

import psycopg2

# Configurações de conexão
conn_params = {
    'dbname': 'seu_banco_de_dados',
    'user': 'seu_usuario',
    'password': 'sua_senha',
    'host': 'localhost',  # ou o IP do seu servidor PostgreSQL
    'port': '5432'        # porta padrão do PostgreSQL
}

# Função para executar um arquivo SQL
def execute_sql_file(filename, conn_params):
    with open(filename, 'r') as file:
        sql = file.read()
    
    # Conectando ao banco de dados
    conn = psycopg2.connect(**conn_params)
    cursor = conn.cursor()
    
    try:
        # Executando o SQL
        cursor.execute(sql)
        conn.commit()
        print("Script SQL executado com sucesso!")
    except Exception as e:
        print(f"Erro ao executar o script SQL: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

# Caminho para o arquivo SQL
sql_file = 'caminho/para/insert_data.sql'

# Executar o arquivo SQL
execute_sql_file(sql_file, conn_params)
