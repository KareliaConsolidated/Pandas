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

print(titanic.Age.head())
# 0    22.0
# 1    38.0
# 2    26.0
# 3    35.0
# 4    35.0
# Name: Age, dtype: float64

print(pd.cut(titanic.Age, bins=[0, 18, 25, 99], labels = ['child', 'young adult', 'adult']).head(10))