import mysql.connector

# Preciso implementar try/except

def init_db(user, password, host, port, database):
    with mysql.connector.connect(user=user, password=password, host=host, port=port) as conn:
        with conn.cursor() as cursor:
            cursor.execute('''CREATE DATABASE IF NOT EXISTS %s;''' %(database,))
        conn.commit()

def create_table(user, password, host, port, database, table):
    with mysql.connector.connect(user=user, password=password, host=host, port=port, database=database) as conn:
        with conn.cursor() as cursor:
            cursor.execute('''CREATE TABLE IF NOT EXISTS %s (
                           altitude FLOAT,
                           cep VARCHAR(8),
                           latitude FLOAT,
                           longitude FLOAT,
                           logradouro VARCHAR(100),
                           bairro VARCHAR(50),
                           complemento VARCHAR(50),
                           cidade VARCHAR(50),
                           sigla_estado VARCHAR(2),
                           ddd INTEGER,
                           ibge_code VARCHAR(50));''' %(table,))
        conn.commit()

# Preciso Verificar a possibilidade de utilizar um comando como BULK INSERT do MS SQL Server

def insert_data(user, password, host, port, database, table, list_values):
    with mysql.connector.connect(user=user, password=password, host=host, port=port, database=database) as conn:
        with conn.cursor() as cursor:
            cursor.execute('''INSERT INTO %s (
                           altitude,
                           cep,
                           latitude,
                           longitude,
                           logradouro,
                           bairro,
                           complemento,
                           cidade,
                           sigla_estado,
                           ddd,
                           ibge_code)
                           VALUES(
                           %s,
                           %s,
                           %s,
                           %s,
                           %s,
                           %s,
                           %s,
                           %s,
                           %s,
                           %s,
                           %s);''' %(table,
                                     list_values[0],
                                     list_values[1],
                                     list_values[2],
                                     list_values[3],
                                     list_values[4],
                                     list_values[5],
                                     list_values[6],
                                     list_values[7],
                                     list_values[8],
                                     list_values[9],
                                     list_values[10]))
        conn.commit()

# Para campos onde a entrada é VARCHAR, o conteudo da string deve ser passado: "'conteudo'".
