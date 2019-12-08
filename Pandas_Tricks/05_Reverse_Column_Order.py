# Reverse Column Order
from Datasets import *

print(drinks.loc[:,::-1].head())

#   continent  total_litres_of_pure_alcohol  wine_servings  spirit_servings  beer_servings      country
# 0      Asia                           0.0              0                0              0  Afghanistan
# 1    Europe                           4.9             54              132             89      Albania
# 2    Africa                           0.7             14                0             25      Algeria
# 3    Europe                          12.4            312              138            245      Andorra
# 4    Africa                           5.9             45               57            217       Angola