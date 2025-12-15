import os
import pandas as pd

from get_data import get_data_from_csv
from medallion import create_layer

PATH_LAYERS = './data'
PATH_CEP = './data/raw_data/lista_ceps.csv'

# creating folders bronze_layer, silver_layer and gold_layer:

create_layer(['bronze', 'silver', 'gold'], PATH_LAYERS)

# populating bronze layer with cep's list:

df = get_data_from_csv(PATH_CEP)

if 'CEP_bronze.csv' not in os.listdir('./data/bronze_layer'):
    df.to_csv('./data/bronze_layer/CEP_bronze.csv', index=False)
