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

# To Get the Numerical Summary of the Data
print(titanic.describe())
# 		 PassengerId    Survived      Pclass         Age       SibSp       Parch        Fare
# count   891.000000  891.000000  891.000000  714.000000  891.000000  891.000000  891.000000
# mean    446.000000    0.383838    2.308642   29.699118    0.523008    0.381594   32.204208
# std     257.353842    0.486592    0.836071   14.526497    1.102743    0.806057   49.693429
# min       1.000000    0.000000    1.000000    0.420000    0.000000    0.000000    0.000000
# 25%     223.500000    0.000000    2.000000   20.125000    0.000000    0.000000    7.910400
# 50%     446.000000    0.000000    3.000000   28.000000    0.000000    0.000000   14.454200
# 75%     668.500000    1.000000    3.000000   38.000000    1.000000    0.000000   31.000000
# max     891.000000    1.000000    3.000000   80.000000    8.000000    6.000000  512.329200

print(titanic.describe().loc['min':'max'])
# 	   PassengerId  Survived  Pclass     Age  SibSp  Parch      Fare
# min          1.0       0.0     1.0   0.420    0.0    0.0    0.0000
# 25%        223.5       0.0     2.0  20.125    0.0    0.0    7.9104
# 50%        446.0       0.0     3.0  28.000    0.0    0.0   14.4542
# 75%        668.5       1.0     3.0  38.000    1.0    0.0   31.0000
# max        891.0       1.0     3.0  80.000    8.0    6.0  512.3292

print(titanic.describe().loc['min':'max','Pclass':'Parch'])
# 	   Pclass     Age  SibSp  Parch
# min     1.0   0.420    0.0    0.0
# 25%     2.0  20.125    0.0    0.0
# 50%     3.0  28.000    0.0    0.0
# 75%     3.0  38.000    1.0    0.0
# max     3.0  80.000    8.0    6.0