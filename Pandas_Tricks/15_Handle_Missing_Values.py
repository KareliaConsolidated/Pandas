import pandas as pd

df_ufo = pd.read_csv('Datasets/ufo.csv')

print(df_ufo.head())

#                    City Colors Reported Shape Reported State             Time
# 0                Ithaca             NaN       TRIANGLE    NY   6/1/1930 22:00
# 1           Willingboro             NaN          OTHER    NJ  6/30/1930 20:00
# 2               Holyoke             NaN           OVAL    CO  2/15/1931 14:00
# 3               Abilene             NaN           DISK    KS   6/1/1931 13:00
# 4  New York Worlds Fair             NaN          LIGHT    NY  4/18/1933 19:00

print(df_ufo.isna().sum())

# City                  25
# Colors Reported    15359
# Shape Reported      2644
# State                  0
# Time                   0
# dtype: int64

print(df_ufo.isna().mean())

# City               0.001371
# Colors Reported    0.842004
# Shape Reported     0.144948
# State              0.000000
# Time               0.000000
# dtype: float64

# Drop Column that has any missing values
print(df_ufo.dropna(axis='columns').head())
#   State             Time
# 0    NY   6/1/1930 22:00
# 1    NJ  6/30/1930 20:00
# 2    CO  2/15/1931 14:00
# 3    KS   6/1/1931 13:00
# 4    NY  4/18/1933 19:00

# Keep the Column in Which 90% of Values are not missing
print(df_ufo.dropna(thresh=len(df_ufo) * 0.90, axis='columns').head())
#                    City State             Time
# 0                Ithaca    NY   6/1/1930 22:00
# 1           Willingboro    NJ  6/30/1930 20:00
# 2               Holyoke    CO  2/15/1931 14:00
# 3               Abilene    KS   6/1/1931 13:00
# 4  New York Worlds Fair    NY  4/18/1933 19:00