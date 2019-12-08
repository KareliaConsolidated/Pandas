# Convert Strings to Numbers
import pandas as pd

df = pd.DataFrame({
	'col_one':['1.1','2.2','3.3'],
	'col_two':['4.4','5.5','6.6'],
	'col_three':['7.7','8.8','-']
	})

print(df)

#  col_one col_two col_three
# 0     1.1     4.4       7.7
# 1     2.2     5.5       8.8
# 2     3.3     6.6         -

print(df.dtypes)

# col_one      object
# col_two      object
# col_three    object
# dtype: object

print(df.astype({'col_one':'float','col_two':'float'}).dtypes) # If third column was included, it would result in error
# dtype: object
# col_one      float64
# col_two      float64
# col_three     object
# dtype: object

print(pd.to_numeric(df.col_three, errors = 'coerce')) # It Will Convert it to Numeric Column, and replace invalid data to NaN
# dtype: object
# 0    7.7
# 1    8.8
# 2    NaN
# Name: col_three, dtype: float64

print(pd.to_numeric(df.col_three, errors = 'coerce').fillna(0))
# 0    7.7
# 1    8.8
# 2    0.0
# Name: col_three, dtype: float64

print(df.apply(pd.to_numeric, errors='coerce').fillna(0))
#    col_one  col_two  col_three
# 0      1.1      4.4        7.7
# 1      2.2      5.5        8.8
# 2      3.3      6.6        0.0
print(df.dtypes)
# col_one      object
# col_two      object
# col_three    object
# dtype: object
