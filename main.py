import numpy as np
import os
import pandas as pd
import requests
import time

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


# Acessar e ler os dados do arquivo csv:
source_cep_df = pd.DataFrame(pd.read_csv(CSV_PATH))

# Chamar a função cep_format para alterar o cep de '00000-000' para '00000000' para usar na requisição:
cep_format(source_cep_df)

# Fazer a requisição para a API CEP Aberto
for x in source_cep_df['cep']: # Usar esse loop na versão final
    pass

response_dict = {'altitude': [],
                 'cep': [],
                 'latitude': [],
                 'longitude': [],
                 'logradouro': [],
                 'bairro': [],
                 'complemento': [],
                 'cidade': [],
                 'ddd': [],
                 'ibge_id': [],
                 'estado_sigla': []}

for i in range(1):
    cep = source_cep_df['cep'].loc[i]
    response = get_data_from_api(cep, TOKEN).json()
    norm_response = pd.json_normalize(response)
    
    response_dict['altitude'].append(norm_response['altitude'].loc[0])
    response_dict['cep'].append(norm_response['cep'].loc[0])
    response_dict['latitude'].append(norm_response['latitude'].loc[0])
    response_dict['longitude'].append(norm_response['longitude'].loc[0])
    response_dict['logradouro'].append(norm_response['logradouro'].loc[0])
    response_dict['bairro'].append(norm_response['bairro'].loc[0])
    response_dict['complemento'].append(norm_response['complemento'].loc[0])
    response_dict['cidade'].append(norm_response['cidade.nome'].loc[0])
    response_dict['ddd'].append(norm_response['cidade.ddd'].loc[0])
    response_dict['ibge_id'].append(norm_response['cidade.ibge'].loc[0])
    response_dict['estado_sigla'].append(norm_response['estado.sigla'].loc[0])
    
    time.sleep(1)

final_df = pd.DataFrame(response_dict)
print(final_df.head(5))