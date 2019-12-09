import pandas as pd

orders = pd.read_csv('Datasets/chipotle.tsv', sep='\t')
print(orders.head(10))
#  order_id  quantity                              item_name                                 choice_description item_price
# 0         1         1           Chips and Fresh Tomato Salsa                                                NaN     $2.39 
# 1         1         1                                   Izze                                       [Clementine]     $3.39 
# 2         1         1                       Nantucket Nectar                                            [Apple]     $3.39 
# 3         1         1  Chips and Tomatillo-Green Chili Salsa                                                NaN     $2.39 
# 4         2         2                           Chicken Bowl  [Tomatillo-Red Chili Salsa (Hot), [Black Beans...    $16.98 
# 5         3         1                           Chicken Bowl  [Fresh Tomato Salsa (Mild), [Rice, Cheese, Sou...    $10.98 
# 6         3         1                          Side of Chips                                                NaN     $1.69 
# 7         4         1                          Steak Burrito  [Tomatillo Red Chili Salsa, [Fajita Vegetables...    $11.75 
# 8         4         1                       Steak Soft Tacos  [Tomatillo Green Chili Salsa, [Pinto Beans, Ch...     $9.25 
# 9         5         1                          Steak Burrito  [Fresh Tomato Salsa, [Rice, Black Beans, Pinto...     $9.25 
orders['numeric_item_price'] = orders.item_price.str.split('$',expand=True)[1]

orders = orders.astype({'numeric_item_price':'float'})

print(orders.groupby('order_id').numeric_item_price.sum().head())
# order_id
# 1    11.56
# 2    16.98
# 3    12.67
# 4    21.00
# 5    13.70
# Name: numeric_item_price, dtype: float64

orders['total_price'] = orders.groupby('order_id').numeric_item_price.transform('sum')

orders['percent_of_total'] = orders.numeric_item_price / orders.total_price

print(orders.head())