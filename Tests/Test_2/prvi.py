import csv
import pandas as pd

# Reading data from CSV file into DataFrame
data = pd.read_csv('/Users/danilakardashevkii/Developer/Python/UDG/Coinis/Tests/Test_2/Ad_table.csv') 

min_price = data['Price'].min()
max_price = data['Price'].max()
print("max price:", max_price)
print("min price:", min_price)

# Computing the average value
average_price = data['Price'].mean()
print("average_price 'price':", average_price)

# Percentage difference
percentage_difference = ((max_price - average_price) / average_price) * 100
print("Percentage difference:", percentage_difference)

# Normalizing 'Price'
normalized_prices = [(price - min_price) / (max_price - min_price) for price in data['Price']]
print("Normalized 'Price' column:", normalized_prices)

# Excluding columns with string data type
numeric_data = data.select_dtypes(include=['int64', 'float64'])

# Computing the correlation matrix between all pairs of numerical columns
correlation_matrix = numeric_data.corr()

# Finding the column with the highest positive correlation
max_positive_correlation_column = correlation_matrix.idxmax().idxmax()
max_positive_correlation_value = correlation_matrix.max().max()
print("Column with the highest positive correlation:", max_positive_correlation_column)
print("Correlation value:", max_positive_correlation_value)

# Finding the column with the highest negative correlation
min_negative_correlation_column = correlation_matrix.idxmin().idxmin()
min_negative_correlation_value = correlation_matrix.min().min()
print("Column with the highest negative correlation:", min_negative_correlation_column)
print("Correlation value:", min_negative_correlation_value)
