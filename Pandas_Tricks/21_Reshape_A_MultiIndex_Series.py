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

print(titanic.Survived.mean()) # 0.3838383838383838

print(titanic.groupby('Sex').Survived.mean())
# Sex
# female    0.742038
# male      0.188908
# Name: Survived, dtype: float64

print(titanic.groupby(['Sex','Pclass']).Survived.mean())
# Sex     Pclass
# female  1         0.968085
#         2         0.921053
#         3         0.500000
# male    1         0.368852
#         2         0.157407
#         3         0.135447
# Name: Survived, dtype: float64

print(titanic.groupby(['Sex','Pclass']).Survived.mean().unstack())
# Pclass         1         2         3
# Sex                                 
# female  0.968085  0.921053  0.500000
# male    0.368852  0.157407  0.135447