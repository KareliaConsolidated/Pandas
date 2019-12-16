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
print(ted.event.value_counts().head())

print(ted.groupby('event').views.agg(['count','mean','sum']).sort_values('sum').tail())
# TEDxNorrkoping        6569493.0
# TEDxCreativeCoast     8444981.0
# TEDxBloomington       9484259.5
# TEDxHouston          16140250.5
# TEDxPuget Sound      34309432.0 <-
# Name: views, dtype: float64
# TEDxPuget Sound have 34 Mil. Views Per Talks
#                 count          mean        sum
# event                                         
# TED2006            45  3.274345e+06  147345533
# TED2015            75  2.011017e+06  150826305
# TEDGlobal 2013     66  2.584163e+06  170554736
# TED2014            84  2.072874e+06  174121423
# TED2013            77  2.302700e+06  177307937

###### UNPACK THE RATINGS DATA
print(ted.ratings.head())

# Looking at First Row
print(ted.loc[0, 'ratings']) or print(ted.ratings[0])
#[{'id': 7, 'name': 'Funny', 'count': 19645}, {'id': 1, 'name': 'Beautiful', 'count': 4573}, {'id': 9, 'name': 'Ingenious', 'count': 6073}, {'id': 3, 'name': 'Courageous', 'count': 3253}, {'id': 11, 'name': 'Longwinded', 'count': 387}, {'id': 2, 'name': 'Confusing', 'count': 242}, {'id': 8, 'name': 'Informative', 'count': 7346}, {'id': 22, 'name': 'Fascinating', 'count': 10581}, {'id': 21, 'name': 'Unconvincing', 'count': 300}, {'id': 24, 'name': 'Persuasive', 'count': 10704}, {'id': 23, 'name': 'Jaw-dropping', 'count': 4439}, {'id': 25, 'name': 'OK', 'count': 1174}, {'id': 26, 'name': 'Obnoxious', 'count': 209}, {'id': 10, 'name': 'Inspiring', 'count': 24924}]

print(type(ted.ratings[0])) # str - String Representation of Dictionary

import ast # Abstract Syntax Tree, to unpack string of dictionary

print(type(ast.literal_eval('[1,2,3]'))) # List

def str_to_list(ratings_str):
	return ast.literal_eval(ratings_str)

print(str_to_list(ted.ratings[0]))
# [{'id': 7, 'name': 'Funny', 'count': 19645}, {'id': 1, 'name': 'Beautiful', 'count': 4573}, {'id': 9, 'name': 'Ingenious', 'count': 6073}, {'id': 3, 'name': 'Courageous', 'count': 3253}, {'id': 11, 'name': 'Longwinded', 'count': 387}, {'id': 2, 'name': 'Confusing', 'count': 242}, {'id': 8, 'name': 'Informative', 'count': 7346}, {'id': 22, 'name': 'Fascinating', 'count': 10581}, {'id': 21, 'name': 'Unconvincing', 'count': 300}, {'id': 24, 'name': 'Persuasive', 'count': 10704}, {'id': 23, 'name': 'Jaw-dropping', 'count': 4439}, {'id': 25, 'name': 'OK', 'count': 1174}, {'id': 26, 'name': 'Obnoxious', 'count': 209}, {'id': 10, 'name': 'Inspiring', 'count': 24924}]

print(ted.ratings.apply(str_to_list).head())
print(ted.ratings.apply(ast.literal_eval).head())
ted['ratings_list']=ted.ratings.apply(lambda x: ast.literal_eval(x))
# 0    [{'id': 7, 'name': 'Funny', 'count': 19645}, {...
# 1    [{'id': 7, 'name': 'Funny', 'count': 544}, {'i...
# 2    [{'id': 7, 'name': 'Funny', 'count': 964}, {'i...
# 3    [{'id': 3, 'name': 'Courageous', 'count': 760}...
# 4    [{'id': 9, 'name': 'Ingenious', 'count': 3202}...
# Name: ratings, dtype: object
print(type(ted['ratings_list'][0])) # list

#### COUNT THE TOTAL NUMBER OF RATINGS RECEIVED BY EACH TALK
# New column named "num_ratings"	
# Bonus:
# For each talk, calculate the percentage of ratings that were negative.
# For each talk, calculate the average number of ratings it received per day since it was published.

print(ted.ratings_list[0])

def get_num_ratings(list_of_dicts):
	num = 0
	for d in list_of_dicts:
		num += d['count']
	return num

ted['num_ratings'] = ted.ratings_list.apply(get_num_ratings)
print(ted.num_ratings.describe())
# count     2550.000000
# mean      2436.408235
# std       4226.795631
# min         68.000000
# 25%        870.750000
# 50%       1452.500000
# 75%       2506.750000
# max      93850.000000
# Name: num_ratings, dtype: float64

def get_negative_ratings(list_of_dicts):
	neg_list = ['Ingenious','Longwinded','Confusing','Unconvincing','Obnoxious']
	num = 0
	for d in list_of_dicts:
		if d['name'] in neg_list:
			num += d['count']
	return num

def calculate_percentage_neg(list_of_dicts):
	return get_negative_ratings(list_of_dicts) / get_num_ratings(list_of_dicts) * 100

print(ted.ratings_list.apply(calculate_percentage_neg))

##### Which occupations deliver the funniest TED talks on average?
# Bonus : 
# For each talk, calculate the most frequent rating
# For each talk, clean the occupation data so that there's only once occupation per talk
def get_funny_ratings(list_of_dicts):
	num = 0
	for d in list_of_dicts:
		if d['name'] == "Funny":
			num += d['count']
	return num

ted['funny_ratings'] = ted.ratings_list.apply(get_funny_ratings)
print(ted['funny_ratings'].head())

def calculate_percentage_funny(list_of_dicts):
	return get_funny_ratings(list_of_dicts) / get_num_ratings(list_of_dicts) * 100

ted['funny_rate'] = ted.ratings_list.apply(calculate_percentage_funny)
print(ted.funny_rate.head())
print(ted.sort_values('funny_rate').speaker_occupation.tail(10))