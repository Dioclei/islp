import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

csv_path = Path(__file__).parents[2] / 'data' / 'Auto.csv'
Auto = pd.read_csv(
    csv_path,
    na_values=['?']
)

# Numerical Summaries:

# use describe() to produce a summary of each column in a dataframe
print(Auto[['mpg', 'weight']].describe())
print(Auto['cylinders'].describe())
print(Auto['mpg'].describe())


# Plotting with Pandas:

# fig, ax = plt.subplots(figsize=(8,8))
# ax.plot(Auto['horsepower'], Auto['mpg'], 'o') # access dataframe directly for plotting
ax = Auto.plot.scatter('horsepower', 'mpg') # or use plotting methods directly from the dataframe
ax.set_title('Horsepower vs MPG')
fig = ax.figure
# fig.savefig('horsepower_mpg.png') # access the figure from the axes to save it

# we can instruct the dataframe to plot to a particular axes object
fig, axes = plt.subplots(ncols=3, figsize=(15, 5))
Auto.plot.scatter('horsepower', 'mpg', ax=axes[1])

# cylinders variable
fig, ax = plt.subplots(ncols=3, figsize=(15, 5))
# print(Auto.cylinders.dtype) # int64 - but actually doesn't have that many values
Auto.cylinders = pd.Series(Auto.cylinders, dtype='category') # update it to a qualitative value
Auto.boxplot('mpg', by='cylinders', ax=ax[0])
Auto.hist('mpg', ax=ax[1])
Auto.hist('mpg', color='red', bins=12, ax=ax[2])

# scatter matrix, for visualizing pairwise relationships (all / a subset)
pd.plotting.scatter_matrix(Auto)
pd.plotting.scatter_matrix(Auto[['mpg', 'displacement', 'weight']])

plt.show()


