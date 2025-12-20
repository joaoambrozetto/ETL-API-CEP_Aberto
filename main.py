import numpy as np
import os
import pandas as pd
import requests

from dotenv import load_dotenv

# Carregar variáveis de ambiente

load_dotenv()

TOKEN = os.environ['API_TOKEN']

# Acessar e ler os dados do arquivo csv, criando um dataframe temporário

CSV_PATH = './data/raw_data/lista_ceps.csv'

temp_df = pd.DataFrame(pd.read_csv(CSV_PATH))

# Formatar o CEP de '00000-000' para '00000000' para usar na requisição

for x in range(temp_df.size):
    temp_df.loc[x] = temp_df.loc[x][:5] + temp_df.loc[x][6:]

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

CEP = '13481164'
URL = f'https://www.cepaberto.com/api/v3/cep?cep={CEP}'
headers = {'Authorization': f'Token token={TOKEN}'}
response = requests.get(URL, headers=headers)

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
print(df)