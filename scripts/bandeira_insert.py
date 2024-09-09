import mysql.connector
import os

def conectar_banco():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="grdm9977",
        database="olimpiadasdb"
    )

def inserir_bandeira(nome_arquivo, nome_pais):
    try:
        # Verificar se o arquivo existe
        if not os.path.isfile(nome_arquivo):
            raise FileNotFoundError(f"O arquivo {nome_arquivo} não foi encontrado.")
        
        # Conectar ao banco de dados
        connection = conectar_banco()
        cursor = connection.cursor()
        
        # Ler a imagem em binário
        with open(nome_arquivo, 'rb') as file:
            imagem_binaria = file.read()
        
        # Inserir a imagem no banco de dados
        query = "UPDATE pais SET bandeira = %s WHERE nome = %s"
        values = (imagem_binaria, nome_pais)
        cursor.execute(query, values)
        connection.commit()
        
        print("Imagem inserida com sucesso!")

    except mysql.connector.Error as err:
        print(f"Erro ao inserir a imagem: {err}")

    except FileNotFoundError as err:
        print(err)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Exemplo de uso
inserir_bandeira(r'C:\Users\guilherme\Documents\olimpiadas_bd\static\img\in.svg', 'Inglaterra')
