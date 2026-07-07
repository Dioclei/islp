import numpy as np
import pandas as pd
from pathlib import Path

csv_path = Path(__file__).parents[2] / 'data' / 'Auto.csv'
Auto = pd.read_csv(csv_path)

print(Auto.columns)
print(Auto['horsepower']) # note that horsepower is of dtype 'object' even though it should be int64
print("unique values:")
print(np.unique(Auto['horsepower']))
# notice that '?' is present in the horsepower and this caused all the data values to be read in as 'string' (object).
# # we reimport and provide read_csv with the appropriate na values

Auto = pd.read_csv(
    csv_path,
    na_values=['?']
)
print("---")
print(Auto['horsepower'])
print(Auto.shape)
Auto_new = Auto.dropna()
print(Auto_new.shape)

# indexing dataframes
# index by rows / filtered rows
print(Auto[:3])
idx_80 = Auto['year'] > 80
print(Auto[idx_80])
# index by columns
print(Auto[['mpg', 'horsepower']])

# index column
print(Auto.index) # no index was set when the dataframe was loaded, so the rows are labeled by integer 0 .. 396
Auto_re = Auto.set_index('name') # set the index column
print(Auto_re)
print(Auto_re.columns) # name column is no longer there because we turned it into the index column
# use index column to obtain rows with .loc[]
rows = ['amc rebel sst', 'ford torino']
print(Auto_re.loc[rows])
print(Auto_re.loc['ford galaxie 500', ['mpg', 'origin']]) # index does not need to be unique

# use iloc to retrieve rows and columns by index
print(Auto_re.iloc[[3, 4]])
print(Auto_re.iloc[:, [0, 2, 3]])
print(Auto_re.iloc[[3, 4], [0, 2, 3]])

# more sophisticated selection
# create a data frame consisting of weight and origin of subset of cars with year greater than 80
idx_80 = Auto_re['year'] > 80
print(Auto_re.loc[idx_80, ['weight', 'origin']])
print(Auto_re.loc[lambda df: df['year'] > 80, ['weight', 'origin']]) # can also use a lambda

print(Auto_re.loc[lambda df: (df['displacement'] < 80)
                             & (df.index.str.contains('ford')
                             | df.index.str.contains('datsun')),
                  ['weight', 'origin']
])



