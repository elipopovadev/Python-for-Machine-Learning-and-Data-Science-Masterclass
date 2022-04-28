import pandas as pd
import numpy as np

my_data = pd.read_excel('D:\student-dropna_1.xlsx', index_col='id')

# NA and Missing are customize missing values
my_data = my_data.replace('NA', np.nan)
my_data = my_data.replace('Missing', np.nan)
# And after that:

# 1.Keep only the rows having 2 or more valid data
my_data = my_data.dropna(how='any', axis=0, thresh=2)

# 2.Keep only the rows having 3 or more valid data
my_data = my_data.dropna(how='any', axis=0, thresh=3)

# 3.Keep only columns where 11 or more valid data is available
my_data = my_data.dropna(how='any', axis=1, thresh=11)

# 4.Keep only rows where 70% or more valid data is available
my_data = my_data.dropna(how='any', axis=0, thresh=my_data.shape[1]*0.7)

# 5.Keep only columns where 80% or more valid data is available
my_data = my_data.dropna(how='any', axis=1, thresh=my_data.shape[0]*0.8)

''' 6.How to take the rows where specific column is not NaN
df = df[df['EPS'].notna()]
df = df.dropna(axis = 'index', how = 'all', subset = ['email', 'lastName']) the row to be droped all of two have to be missing'''

''' 7. How to fill in missing data in column:
df['column'] = df['column'].fillna(0)'''

# 8. How to drop all rows that have missing value in all their columns?
my_data = my_data.dropna(axis='index', how='all')
