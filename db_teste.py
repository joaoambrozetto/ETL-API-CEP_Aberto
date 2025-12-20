import mysql.connector
import os

from dotenv import load_dotenv

load_dotenv()

USER = os.environ['MYSQL_USER']
PASSWORD = os.environ['MYSQL_PASSWORD']
HOST = os.environ['MYSQL_HOST']
PORT = os.environ['MYSQL_PORT']

with mysql.connector.connect(user=USER, password=PASSWORD, host=HOST, port=PORT) as conn:
    with conn.cursor() as cursor:
        cursor.execute("CREATE DATABASE IF NOT EXISTS example_db;")
        cursor.execute("DROP DATABASE example_db;")