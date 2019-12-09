import pandas as pd

orders = pd.read_csv('Datasets/chipotle.tsv', sep='\t')
print(orders.head())

# order_id  quantity                              item_name                                 choice_description item_price
# 0         1         1           Chips and Fresh Tomato Salsa                                                NaN     $2.39 
# 1         1         1                                   Izze                                       [Clementine]     $3.39 
# 2         1         1                       Nantucket Nectar                                            [Apple]     $3.39 
# 3         1         1  Chips and Tomatillo-Green Chili Salsa                                                NaN     $2.39 
# 4         2         2                           Chicken Bowl  [Tomatillo-Red Chili Salsa (Hot), [Black Beans...    $16.98 

orders['numeric_item_price'] = orders.item_price.str.split('$',expand=True)[1]
print(orders.head())
# order_id  quantity                              item_name                                 choice_description item_price numeric_item_price
# 0         1         1           Chips and Fresh Tomato Salsa                                                NaN     $2.39               2.39 
# 1         1         1                                   Izze                                       [Clementine]     $3.39               3.39 
# 2         1         1                       Nantucket Nectar                                            [Apple]     $3.39               3.39 
# 3         1         1  Chips and Tomatillo-Green Chili Salsa                                                NaN     $2.39               2.39 
# 4         2         2                           Chicken Bowl  [Tomatillo-Red Chili Salsa (Hot), [Black Beans...    $16.98              16.98 
# pd.to_numeric(orders['numeric_item_price'], errors = 'coerce')

orders = orders.astype({'numeric_item_price':'float'})

print(orders.numeric_item_price.dtype) # float

print(orders[orders.order_id == 1].numeric_item_price.sum()) # 11.56

print(orders.groupby('order_id').numeric_item_price.sum().head())
# order_id
# 1    11.56
# 2    16.98
# 3    12.67
# 4    21.00
# 5    13.70
# Name: numeric_item_price, dtype: float64
print(orders.groupby('order_id').numeric_item_price.agg(['sum','count']).head())
# order_id              
# 1         11.56      4
# 2         16.98      1
# 3         12.67      2
# 4         21.00      2
# 5         13.70      2