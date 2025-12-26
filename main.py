import numpy as np
import os
import pandas as pd
import requests

from dotenv import load_dotenv

from data_manipulation import cep_format, get_data_from_api
from database import init_db, create_table, insert_data


# Carregar variáveis de ambiente:
load_dotenv()

# Constantes:
CSV_PATH = './data/raw_data/lista_ceps.csv'
TOKEN = os.environ['API_TOKEN']
USER = os.environ['MYSQL_USER']
PASSWORD = os.environ['MYSQL_PASSWORD']
HOST = os.environ['MYSQL_HOST']
PORT = os.environ['MYSQL_PORT']


# Acessar e ler os dados do arquivo csv, criando um dataframe temporário:
temp_df = pd.DataFrame(pd.read_csv(CSV_PATH))

# Chamar a função cep_format para alterar o cep de '00000-000' para '00000000' para usar na requisição:
cep_format(temp_df)

# Criar um dataframe vazio para popular com as requisições:

columns = {'altitude': None,
           'cep': None,
           'latitude': None,
           'longitude': None,
           'logradouro': None,
           'bairro': None,
           'complemento': None,
           'cidade': None,
           'estado': None,
           'ddd': None,
           'ibge': None}
df = pd.DataFrame(data=columns, index=[])

# Fazer a requisição para a API CEP Aberto

response = get_data_from_api('13481164', TOKEN)

# Inserir dados do response no DataFrame:
data = response.json()
if 'complemento' not in data.keys():
    df.loc[0] = [data['altitude'],
                 data['cep'],
                 data['latitude'],
                 data['longitude'],
                 data['logradouro'],
                 data['bairro'],
                 np.nan,
                 data['cidade']['nome'],
                 data['estado']['sigla'],
                 data['cidade']['ddd'],
                 data['cidade']['ibge']]
else:
    df.loc[0] = [data['altitude'],
                 data['cep'],
                 data['latitude'],
                 data['longitude'],
                 data['logradouro'],
                 data['bairro'],
                 data['complemento'],
                 data['cidade']['nome'],
                 data['estado']['sigla'],
                 data['cidade']['ddd'],
                 data['cidade']['ibge']]

init_db(USER, PASSWORD, HOST, PORT, 'TesteDB')