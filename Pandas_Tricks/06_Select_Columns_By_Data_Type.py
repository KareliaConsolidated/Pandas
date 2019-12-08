# Select Columns By Data Type
from Datasets import *

print(drinks.dtypes)

# country                          object
# beer_servings                     int64
# spirit_servings                   int64
# wine_servings                     int64
# total_litres_of_pure_alcohol    float64
# continent                        object
# dtype: object

print(drinks.select_dtypes(include='number').head()) # number will select integer and float both

#    beer_servings  spirit_servings  wine_servings  total_litres_of_pure_alcohol
# 0              0                0              0                           0.0
# 1             89              132             54                           4.9
# 2             25                0             14                           0.7
# 3            245              138            312                          12.4
# 4            217               57             45                           5.9

print(drinks.select_dtypes(include='object').head()) # number will select integer and float both

#        country continent
# 0  Afghanistan      Asia
# 1      Albania    Europe
# 2      Algeria    Africa
# 3      Andorra    Europe
# 4       Angola    Africa

print(drinks.select_dtypes(include=['number','category','object']).head()) # number will select integer and float both

#        country  beer_servings  spirit_servings  wine_servings  total_litres_of_pure_alcohol continent
# 0  Afghanistan              0                0              0                           0.0      Asia
# 1      Albania             89              132             54                           4.9    Europe
# 2      Algeria             25                0             14                           0.7    Africa
# 3      Andorra            245              138            312                          12.4    Europe
# 4       Angola            217               57             45                           5.9    Africa

print(drinks.select_dtypes(exclude='number').head())

#        country continent
# 0  Afghanistan      Asia
# 1      Albania    Europe
# 2      Algeria    Africa
# 3      Andorra    Europe
# 4       Angola    Africa