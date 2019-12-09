from glob import glob
import pandas as pd

stock_files = sorted(glob('Datasets/stocks*.csv'))

print(stock_files)
# ['Datasets/stocks.csv', 'Datasets/stocks1.csv', 'Datasets/stocks2.csv', 'Datasets/stocks3.csv']
print(pd.concat(pd.read_csv(file) for file in stock_files))
#          Date   Close    Volume Symbol
# 0  2016-10-03   31.50  14070500   CSCO
# 1  2016-10-03  112.52  21701800   AAPL
# 2  2016-10-03   57.42  19189500   MSFT
# 3  2016-10-04  113.00  29736800   AAPL
# 4  2016-10-04   57.24  20085900   MSFT
# 5  2016-10-04   31.35  18460400   CSCO
# 6  2016-10-05   57.64  16726400   MSFT
# 7  2016-10-05   31.59  11808600   CSCO
# 8  2016-10-05  113.05  21453100   AAPL
# 0  2016-10-03   31.50  14070500   CSCO
# 1  2016-10-03  112.52  21701800   AAPL
# 2  2016-10-03   57.42  19189500   MSFT
# 0  2016-10-04  113.00  29736800   AAPL
# 1  2016-10-04   57.24  20085900   MSFT
# 2  2016-10-04   31.35  18460400   CSCO
# 0  2016-10-05   57.64  16726400   MSFT
# 1  2016-10-05   31.59  11808600   CSCO
# 2  2016-10-05  113.05  21453100   AAPL
print(pd.concat((pd.read_csv(file) for file in stock_files), ignore_index=True))
#     Date   Close    Volume Symbol
# 0   2016-10-03   31.50  14070500   CSCO
# 1   2016-10-03  112.52  21701800   AAPL
# 2   2016-10-03   57.42  19189500   MSFT
# 3   2016-10-04  113.00  29736800   AAPL
# 4   2016-10-04   57.24  20085900   MSFT
# 5   2016-10-04   31.35  18460400   CSCO
# 6   2016-10-05   57.64  16726400   MSFT
# 7   2016-10-05   31.59  11808600   CSCO
# 8   2016-10-05  113.05  21453100   AAPL
# 9   2016-10-03   31.50  14070500   CSCO
# 10  2016-10-03  112.52  21701800   AAPL
# 11  2016-10-03   57.42  19189500   MSFT
# 12  2016-10-04  113.00  29736800   AAPL
# 13  2016-10-04   57.24  20085900   MSFT
# 14  2016-10-04   31.35  18460400   CSCO
# 15  2016-10-05   57.64  16726400   MSFT
# 16  2016-10-05   31.59  11808600   CSCO
# 17  2016-10-05  113.05  21453100   AAPL