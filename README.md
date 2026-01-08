

# ETL - Dados de endereçamento postal
Esse projeto implementa uma pipeline de ETL (Extract, Transform, Load) que lê os CEPS de um arquivo CSV e realiza requisições para a API CEP Aberto. Os dados obtidos na requisição são tratados e inseridos em um Dataframe do Pandas para posterior inserção em um banco de dados MySQL rodando via Docker.

> [!IMPORTANT]
> Estou desenvolvendo esse projeto como uma preparação para um projeto mais ambicioso relacionado com pacotes entregues de um determinado e-commerce.
> A partir de dados de entrega de uma planilha do Google Sheets, o script fará requisições para enriquecê-los e carregá-los no banco de dados utilizando Batch Processing e um Scheduler.
> Os dados obtidos serão utilizados para análise dos dados de entrega (taxa de sucesso, locais que mais compram, causas mais comuns de devolução, etc).

## Tecnologias utilizadas
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat&logo=mysql&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-000000?style=flat&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)

## Rodando localmente
Para executar o pipeline em seu ambiente local basta seguir os passos abaixo:
1. Clone este repositório:
```
git clone https://github.com/joaoambrozetto/ETL-API-CEP_Aberto.git
```
2. No terminal, vá até a pasta do projeto:
```
cd ETL-API-CEP_Aberto
```
3. Inicie o banco de dados MySQL via Docker:
```
docker run --name cep-aberto_mysql -e MYSQL_ROOT_PASSWORD=password -p 3306:3306 -v mysql_data:/var/lib/mysql -d mysql:latest
```
4. Execute o arquivo `main.py`:
```
python3 -m main
```
