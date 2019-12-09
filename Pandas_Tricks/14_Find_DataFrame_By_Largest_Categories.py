import pandas as pd

df_movies = pd.read_csv('Datasets/imdb_1000.csv')

print(df_movies.head())

#  star_rating                     title content_rating   genre  duration                                        actors_list
# 0          9.3  The Shawshank Redemption              R   Crime       142  [u'Tim Robbins', u'Morgan Freeman', u'Bob Gunt...
# 1          9.2             The Godfather              R   Crime       175    [u'Marlon Brando', u'Al Pacino', u'James Caan']
# 2          9.1    The Godfather: Part II              R   Crime       200  [u'Al Pacino', u'Robert De Niro', u'Robert Duv...
# 3          9.0           The Dark Knight          PG-13  Action       152  [u'Christian Bale', u'Heath Ledger', u'Aaron E...
# 4          8.9              Pulp Fiction              R   Crime       154  [u'John Travolta', u'Uma Thurman', u'Samuel L....

counts = df_movies.genre.value_counts()

print(counts)
# Drama        278
# Comedy       156
# Action       136
# Crime        124
# Biography     77
# Adventure     75
# Animation     62
# Horror        29
# Mystery       16
# Western        9
# Sci-Fi         5
# Thriller       5
# Film-Noir      3
# Family         2
# History        1
# Fantasy        1
# Name: genre, dtype: int64

print(counts.nlargest(3))
# Drama     278
# Comedy    156
# Action    136
# Name: genre, dtype: int64

print(counts.nlargest(3).index)
# Index(['Drama', 'Comedy', 'Action'], dtype='object')

print(df_movies[df_movies.genre.isin(counts.nlargest(3).index)].head())
# star_rating                                           title  ... duration                                        actors_list
# 3           9.0                                 The Dark Knight  ...      152  [u'Christian Bale', u'Heath Ledger', u'Aaron E...
# 5           8.9                                    12 Angry Men  ...       96  [u'Henry Fonda', u'Lee J. Cobb', u'Martin Bals...
# 9           8.9                                      Fight Club  ...      139  [u'Brad Pitt', u'Edward Norton', u'Helena Bonh...
# 11          8.8                                       Inception  ...      148  [u'Leonardo DiCaprio', u'Joseph Gordon-Levitt'...
# 12          8.8  Star Wars: Episode V - The Empire Strikes Back  ...      124  [u'Mark Hamill', u'Harrison Ford', u'Carrie Fi...

# [5 rows x 6 columns]