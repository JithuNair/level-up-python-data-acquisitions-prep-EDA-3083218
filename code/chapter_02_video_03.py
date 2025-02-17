import pandas as pd

employees = pd.read_csv('data/level_up_data.csv')

data_types = employees.dtypes

print(data_types)

numeric_columns = employees.columns[(data_types == 'float64') | (data_types == 'int64')]

numeric_columns = numeric_columns[numeric_columns != "separated_ny"]

numeric_employees = employees[numeric_columns]

print(numeric_employees.dtypes)
