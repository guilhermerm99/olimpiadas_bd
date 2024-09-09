import mysql.connector

# Configuração do banco de dados
def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='seu_usuario',   # Substitua pelo seu usuário do MySQL
        password='sua_senha', # Substitua pela sua senha do MySQL
        database='OlimpiadasDB'
    )
    return connection
