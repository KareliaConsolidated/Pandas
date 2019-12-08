# Reduce DataFrame Size
from Datasets import *

drinks.info(memory_usage = 'deep')
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 193 entries, 0 to 192
# Data columns (total 6 columns):
# country                         193 non-null object
# beer_servings                   193 non-null int64
# spirit_servings                 193 non-null int64
# wine_servings                   193 non-null int64
# total_litres_of_pure_alcohol    193 non-null float64
# continent                       193 non-null object
# dtypes: float64(1), int64(3), object(2)
# memory usage: 30.5 KB
# None

# Read Data Which is Required
cols = ['beer_servings', 'continent']
small_drinks = pd.read_csv('Datasets/drinks.csv', usecols = cols)
small_drinks.info(memory_usage='deep')
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 193 entries, 0 to 192
# Data columns (total 2 columns):
# beer_servings    193 non-null int64
# continent        193 non-null object
# dtypes: int64(1), object(1)
# memory usage: 13.7 KB

# Convert Column to Category DataType Which Contains Categorical Data Types
dtypes = {'continent': 'category'}
small_drinks = pd.read_csv('Datasets/drinks.csv', usecols = cols, dtype=dtypes)
small_drinks.info(memory_usage='deep')

# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 193 entries, 0 to 192
# Data columns (total 2 columns):
# beer_servings    193 non-null int64
# continent        193 non-null category
# dtypes: category(1), int64(1)
# memory usage: 2.4 KB