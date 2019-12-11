import pandas as pd
import matplotlib.pyplot as plt

ted = pd.read_csv('Datasets/ted.csv')

print(ted.head())

# print(pd.show_versions()) 

print(ted.shape) # (2550, 17)

print(ted.isna().sum())
# comments              0
# description           0
# duration              0
# event                 0
# film_date             0
# languages             0
# main_speaker          0
# name                  0
# num_speaker           0
# published_date        0
# ratings               0
# related_talks         0
# speaker_occupation    6 <-
# tags                  0
# title                 0
# url                   0
# views                 0
# dtype: int64

print(ted.dtypes)
# comments               int64
# description           object
# duration               int64
# event                 object
# film_date              int64
# languages              int64
# main_speaker          object
# name                  object
# num_speaker            int64
# published_date         int64
# ratings               object
# related_talks         object
# speaker_occupation    object
# tags                  object
# title                 object
# url                   object
# views                  int64
# dtype: object

##### WHICH TALKS PROVOKE THE MOST ONLINE DISCUSSION ?

# Consider the limitations and biases of your data when analyzing it.
print(ted.sort_values('comments').tail())
#       comments                                        description  ...                                                url     views
# 1787      2673  Our consciousness is a fundamental aspect of o...  ...  https://www.ted.com/talks/david_chalmers_how_d...   2162764
# 201       2877  Jill Bolte Taylor got a research opportunity f...  ...  https://www.ted.com/talks/jill_bolte_taylor_s_...  21190883
# 644       3356  Questions of good and evil, right and wrong ar...  ...  https://www.ted.com/talks/sam_harris_science_c...   3433437
# 0         4553  Sir Ken Robinson makes an entertaining and pro...  ...  https://www.ted.com/talks/ken_robinson_says_sc...  47227110
# 96        6404  Richard Dawkins urges all atheists to openly s...  ...  https://www.ted.com/talks/richard_dawkins_on_m...   4374792

ted['comments_per_view'] = ted.comments / ted.views

print(ted.sort_values('comments_per_view').tail())
#      comments                                        description  ...    views comments_per_view
# 954      2492  Janet Echelman found her true voice as an arti...  ...  1832930          0.001360
# 694      1502  Filmmaker Sharmeen Obaid-Chinoy takes on a ter...  ...  1057238          0.001421
# 96       6404  Richard Dawkins urges all atheists to openly s...  ...  4374792          0.001464
# 803       834  David Bismark demos a new system for voting th...  ...   543551          0.001534
# 744       649  Hours before New York lawmakers rejected a key...  ...   292395          0.002220

ted['views_per_comment'] = ted.views / ted.comments

print(ted.sort_values('views_per_comment').head())
#      comments                                        description  duration  ...    views  comments_per_view  views_per_comment
# 744       649  Hours before New York lawmakers rejected a key...       453  ...   292395           0.002220         450.531587
# 803       834  David Bismark demos a new system for voting th...       422  ...   543551           0.001534         651.739808
# 96       6404  Richard Dawkins urges all atheists to openly s...      1750  ...  4374792           0.001464         683.134291
# 694      1502  Filmmaker Sharmeen Obaid-Chinoy takes on a ter...       489  ...  1057238           0.001421         703.886818
# 954      2492  Janet Echelman found her true voice as an arti...       566  ...  1832930           0.001360         735.525682

##### VISUALIZE THE DISTRIBUTION OF COMMENTS
# 1. Choose your plot type based on the question you are answering and the data type(s) you are working with.
# 2. Use pandas as one-liners to iterate through plots quickly
# 3. Try modifing the plot defaults
# 4. Creating Plots invloves decision-making

print(ted[ted.comments >= 1000].shape) # 32,9
################# WAY 01 #################
# ted[ted.comments < 1000].comments.plot(kind='hist')
# OR
################# WAY 02 #################
# ted.query('comments < 1000').comments.plot(kind='hist')
# OR
################# WAY 03 #################
ted.loc[ted.comments < 1000, 'comments'].plot(kind='hist',bins=20)

# plt.show()

# PLOT THE NUMBER OF TALKS THAT TOOK PLACE EACH YEAR
# 1. Read the Documentation
# 2. Use the datetime data type for dates and times
# 3. Check your work as you go
# 4. Consider excluding data if it might not be relevant
print(ted.event.sample(10)) # Random 10 Samples
print(ted.film_date.head()) # Unix TimeStamp
# 0    1140825600
# 1    1140825600
# 2    1140739200
# 3    1140912000
# 4    1140566400
# Name: film_date, dtype: int64

print(pd.to_datetime(ted.film_date, unit='s').head())
# 0   2006-02-25
# 1   2006-02-25
# 2   2006-02-24
# 3   2006-02-26
# 4   2006-02-22
# Name: film_date, dtype: datetime64[ns]
ted['film_datetime'] = pd.to_datetime(ted.film_date, unit='s')

print(ted[['event','film_datetime']].sample(5))
#                   event film_datetime
# 2140  TEDxCreativeCoast    2015-05-01
# 1906     TEDGlobal 2014    2014-10-06
# 148             TED2007    2007-03-03
# 1202         TEDxChange    2012-04-05
# 1492            TED2013    2013-02-26

print(ted.film_datetime.dt.year.head()) #dayofyear
# 0    2006
# 1    2006
# 2    2006
# 3    2006
# 4    2006
# Name: film_datetime, dtype: int64

print(ted.film_datetime.dt.year.value_counts().sort_index().plot())
# 2013    270
# 2011    270
# 2010    267
# 2012    267
# 2016    246
# 2015    239
# 2014    237
# 2009    232
# 2007    114
# 2017     98
# 2008     84
# 2005     66
# 2006     50
# 2003     33
# 2004     33
# 2002     27
# 1998      6
# 2001      5
# 1983      1
# 1991      1
# 1994      1
# 1990      1
# 1984      1
# 1972      1
# Name: film_datetime, dtype: int64

# plt.show()

##### What were the "BEST" events in TED history to attend ? 