import pandas as pd

# 1
points = [10000, 20000, 4000, 5000]
names = ['Andrew', 'Maria', 'Ana', 'George']
my_data = list(zip(names, points))
rows = ['Canada', 'Bulgaria', 'UK', 'Belgium']
cols = ['HR', 'Points']
df = pd.DataFrame(data=my_data, columns=cols, index=rows)
print(df)

# 2
my_new_data = [['Andrew', 10000], ['Maria', 20000],
               ['Ana', 4000], ['George', 5000]]
new_df = pd.DataFrame(data=my_new_data, columns=cols, index=rows)
print(new_df)

# 3
my_df1 = pd.read_csv('C:/Users/eli/Desktop/listings.csv')
print(my_df1.head(100))
print(my_df1.tail(100))
print(my_df1.columns)
print(my_df1.index)
print(my_df1.info())

colums = ['id', 'name']
print(my_df1[colums])  # grab the colums

print(my_df1.iloc[0])  # grab the first row based on integer index
print(my_df1.iloc[0:4])  # grab the first four row
# print(my_df1.loc['...']) # grab the first row based on label index
