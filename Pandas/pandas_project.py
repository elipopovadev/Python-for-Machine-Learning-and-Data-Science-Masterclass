import pandas as pd
import numpy as np

hotels = pd.read_csv("C:/Users/eli/Desktop/hotel_booking_data.csv")

# How many rows are there?
number_rows = hotels.count(axis=0)
print(number_rows)


# Is there any missing data? If so, which column has the most missing data?
# children - 4; country - 488; agent - 16340; company - 112 593
checker = hotels.isna().sum()
print(checker)


# 'company' has the most missing data
print(hotels.count().idxmin())


# Drop the "company" column from the dataset
hotels = hotels.drop('company', axis=1)


# What are the top 5 most common country codes in the dataset?
n = 5
print(hotels['country'].value_counts()[:n])


# What is the name of the person who paid the highes ADR(average daily rate)? How much was their ADR?
# or another solution: hotels.sort_values('adr', ascending=False)[['adr', 'name']].iloc[0]
max_adr = hotels['adr'].nlargest(1)  # 5400
rows_with_max_adr = hotels.loc[hotels['adr'] == int(max_adr)]  # get the row
print(rows_with_max_adr[['name', 'adr']])


# What is the mean adr(average daily rate) across all the hotel stays in the dataset?
mean_adr = hotels['adr'].mean()
print(mean_adr)


# What is the average number of nights for a stay across the entire data set?
sum_columns = hotels['stays_in_week_nights'] + \
    hotels['stays_in_weekend_nights']
print(round(sum_columns.mean(), 2))


# What is the average total cost for a stay in the dataset
avg_total_cost = ((hotels['stays_in_week_nights'] +
                   hotels['stays_in_weekend_nights']) * hotels['adr']).mean()
print(round(avg_total_cost, 2))


# What are the names and emails of people who made exactly 5 "Special Requests"?
total_of_special_requests = 5

rows_with_exactly_five_spec_requests = hotels.loc[hotels['total_of_special_requests'] == int(
    total_of_special_requests)]  # get all rows with exactly 5 special requests
print(rows_with_exactly_five_spec_requests[['name', 'email']])


# What percentage of hotel stays were classified as "repeat guests"?
repeat_guests = sum(hotels['is_repeated_guest'] == 1) / len(hotels) * 100
print(repeat_guests)


# What are the names of the people who had booked the most number children and babies for their stay?
hotels['total_kids'] = (hotels['children'] + hotels['babies'])

the_most_kids_index = hotels['total_kids'].nlargest(3).index
print(hotels.iloc[the_most_kids_index][['name', 'adults',
      'total_kids', 'babies', 'children']])  # select rows based on list index


# What are the top 5 most common last name in the dataset?
n = 5
print(hotels['name'].str.split().str[1].value_counts()[:n])


# What are the top 3 most common area code in the phone numbers?
n = 3
print(hotels['phone-number'].str.split('-').str[0].value_counts()[:n])


# How many arrivals took place between the 1st and the 15th of the month (inclusive of 1 and 15)?
print(sum(hotels['arrival_date_day_of_month'].isin(range(1, 16))))


# Create a table for counts for each day of the week that people arrived.
def convert(day, month, year):
    return f"{day}-{month}-{year}"


hotels['date'] = np.vectorize(convert)(
    hotels['arrival_date_day_of_month'], hotels['arrival_date_month'], hotels['arrival_date_year'])

hotels['date'] = pd.to_datetime(hotels['date'])

print(hotels['date'].dt.day_name().value_counts())
