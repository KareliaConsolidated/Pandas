import pandas as pd

titanic = pd.read_csv('Datasets/titanic_train.csv')

print(titanic.head())
# PassengerId  Survived  Pclass                                               Name     Sex  ...  Parch            Ticket     Fare Cabin  Embarked
# 0            1         0       3                            Braund, Mr. Owen Harris    male  ...      0         A/5 21171   7.2500   NaN         S
# 1            2         1       1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  ...      0          PC 17599  71.2833   C85         C
# 2            3         1       3                             Heikkinen, Miss. Laina  female  ...      0  STON/O2. 3101282   7.9250   NaN         S
# 3            4         1       1       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  ...      0            113803  53.1000  C123         S
# 4            5         0       3                           Allen, Mr. William Henry    male  ...      0            373450   8.0500   NaN         S
# [5 rows x 12 columns]

print(titanic.pivot_table(index='Sex', columns='Pclass', values='Survived', aggfunc='mean'))
# Pclass         1         2         3
# Sex                                 
# female  0.968085  0.921053  0.500000
# male    0.368852  0.157407  0.135447

print(titanic.pivot_table(index='Sex', columns='Pclass', values='Survived', aggfunc='mean', margins=True))
# Pclass         1         2         3       All
# Sex                                           
# female  0.968085  0.921053  0.500000  0.742038
# male    0.368852  0.157407  0.135447  0.188908
# All     0.629630  0.472826  0.242363  0.383838

print(titanic.pivot_table(index='Sex', columns='Pclass', values='Survived', aggfunc='count', margins=True))
# Pclass    1    2    3  All
# Sex                       
# female   94   76  144  314
# male    122  108  347  577
# All     216  184  491  891
