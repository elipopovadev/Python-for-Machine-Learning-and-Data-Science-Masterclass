import pandas as pd

# making data frame from csv file
data = pd.read_csv("employees.csv")

# creating filters of bool series from isin()
filter1 = data["Gender"].isin(["Female"])
filter2 = data["Team"].isin(["Engineering", "Distribution", "Finance"])

# displaying data with both filter applied and mandatory
data[filter1 & filter2]

# print(sum(hotels['arrival_date_day_of_month'].isin(range(1, 16))))
