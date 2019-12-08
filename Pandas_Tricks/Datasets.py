import pandas as pd
import numpy as np

drinks = pd.read_csv('Datasets/drinks.csv')
movies = pd.read_csv('Datasets/imdb_1000.csv')
orders = pd.read_csv('Datasets/chipotle.tsv', sep='\t')
orders['item_price'] = orders.item_price.str.replace('$', '').astype('float')
stocks = pd.read_csv('Datasets/stocks.csv', parse_dates=['Date'])
titanic = pd.read_csv('Datasets/titanic_train.csv')
ufo = pd.read_csv('Datasets/ufo.csv')