import os
import pandas as pd
import requests

from dotenv import load_dotenv


load_dotenv()

TOKEN = os.environ["TOKEN"]


def get_data_from_csv(path):
    return pd.DataFrame(pd.read_csv(path))


def get_data_from_api(cep):
    URL = f'https://www.cepaberto.com/api/v3/cep?cep={cep}'
    headers = {'Authorization': f'Token token={TOKEN}'}
    response = requests.get(URL, headers=headers)
    return response.json()
    
'''
O limite de requisições da API Cep Aberto é 1/segundo, limitada a 10.000 por dia
Necessário configurar variáveis de ambiente para chave de API
Importar time e usar time.sleep(1) para diminuir a velocidade das requisições
'''

if __name__ == '__main__':
    print(__name__)

