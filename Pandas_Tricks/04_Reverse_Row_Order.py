# Reverse Row Order
from Datasets import *

print(drinks.head())

#        country  beer_servings  spirit_servings  wine_servings  total_litres_of_pure_alcohol continent
# 0  Afghanistan              0                0              0                           0.0      Asia
# 1      Albania             89              132             54                           4.9    Europe
# 2      Algeria             25                0             14                           0.7    Africa
# 3      Andorra            245              138            312                          12.4    Europe
# 4       Angola            217               57             45                           5.9    Africa

print(drinks.loc[::-1].head())

#        country  beer_servings  spirit_servings  wine_servings  total_litres_of_pure_alcohol      continent
# 192   Zimbabwe             64               18              4                           4.7         Africa
# 191     Zambia             32               19              4                           2.5         Africa
# 190      Yemen              6                0              0                           0.1           Asia
# 189    Vietnam            111                2              1                           2.0           Asia
# 188  Venezuela            333              100              3                           7.7  South America

print(drinks.loc[::-1].reset_index(drop=True).head())

#      country  beer_servings  spirit_servings  wine_servings  total_litres_of_pure_alcohol      continent
# 0   Zimbabwe             64               18              4                           4.7         Africa
# 1     Zambia             32               19              4                           2.5         Africa
# 2      Yemen              6                0              0                           0.1           Asia
# 3    Vietnam            111                2              1                           2.0           Asia
# 4  Venezuela            333              100              3                           7.7  South America