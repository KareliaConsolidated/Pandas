import pandas as pd

df = pd.DataFrame({'col_name':['a','b','c'], 'col_two':[[10,40],[20,50],[30,60]]})
print(df)

#   col_name   col_two
# 0        a  [10, 40]
# 1        b  [20, 50]
# 2        c  [30, 60]

df_new = df.col_two.apply(pd.Series)
print(df_new)
#     0   1
# 0  10  40
# 1  20  50
# 2  30  60

print(pd.concat([df, df_new], axis='columns'))
# 	col_name   col_two   0   1
# 0        a  [10, 40]  10  40
# 1        b  [20, 50]  20  50
# 2        c  [30, 60]  30  60