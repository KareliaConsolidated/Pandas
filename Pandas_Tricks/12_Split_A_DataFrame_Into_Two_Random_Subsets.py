import pandas as pd

df_movies = pd.read_csv('Datasets/imdb_1000.csv')

print(len(df_movies)) #979

df_movies_1 = df_movies.sample(frac=0.75, random_state=1234)
df_movies_2 = df_movies.drop(df_movies_1.index)

print(len(df_movies_1)) # 734
print(len(df_movies_2)) # 245
print(len(df_movies_1) + len(df_movies_2)) # 979

print(df_movies_1.index.sort_values())
# Int64Index([  0,   2,   5,   6,   7,   8,   9,  11,  13,  16,
#             ...
#             966, 967, 969, 971, 972, 974, 975, 976, 977, 978],
#            dtype='int64', length=734)
print(df_movies_2.index.sort_values())
# Int64Index([  1,   3,   4,  10,  12,  14,  15,  18,  26,  30,
#             ...
#             931, 934, 937, 941, 950, 954, 960, 968, 970, 973],
#            dtype='int64', length=245)