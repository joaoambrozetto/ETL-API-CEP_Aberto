import requests


# Formatar o CEP de '00000-000' para '00000000' para usar na requisição
def cep_format(df):
    for x in range(df.size):
        df.loc[x, 'cep'] = df.loc[x, 'cep'][:5] + df.loc[x, 'cep'][6:]

# Fazer a requisição para a API CEP Aberto
def get_data_from_api(cep, token):
    URL = f'https://www.cepaberto.com/api/v3/cep?cep={cep}'
    headers = {'Authorization': f'Token token={token}'}
    
    return requests.get(URL, headers=headers)