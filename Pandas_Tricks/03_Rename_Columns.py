from Datasets import *

df0 = pd.DataFrame({'col one':[100, 200], 'col two': [300, 400]})

print(df0)

#    col one  col two
# 0      100      300
# 1      200      400

df0 = df0.rename({'col one':'col_one', 'col two': 'col_two'}, axis = 'columns') # Old Column : New Column

# If changing all columns name, its better to use:
df0.columns = ['col_one', 'col_two']

# If we want to change only space with underscores
df0.columns = df0.columns.str.replace(' ','_')

print(df0)

#    col_one  col_two
# 0      100      300
# 1      200      400

# If we want to add only prefix or suffix

print(df0.add_prefix('X_'))

#    X_col_one  X_col_two
# 0        100        300
# 1        200        400

print(df0.add_suffix('_Y'))

# 	col_one_Y  col_two_Y
# 0        100        300
# 1        200        400