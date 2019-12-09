from glob import glob
import pandas as pd

drinks = sorted(glob('Datasets/drinks*.csv'))

print(pd.concat((pd.read_csv(file) for file in drinks), axis='columns').head())

# country  beer_servings  spirit_servings wine_servings  ...  spirit_servings wine_servings total_litres_of_pure_alcohol  continent
# 0  Afghanistan              0                0             0  ...                0             0                          0.0       Asia
# 1      Albania             89              132            54  ...              132            54                          4.9     Europe
# 2      Algeria             25                0            14  ...                0            14                          0.7     Africa
# 3      Andorra            245              138           312  ...              138           312                         12.4     Europe
# 4       Angola            217               57            45  ...               57            45                          5.9     Africa
