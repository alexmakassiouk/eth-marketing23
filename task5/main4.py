import pandas as pd
from IPython.display import display
import numpy as np

def get_data():
    data = pd.read_csv('../data.csv', sep=';')
    return data

# Explore data from get_data()
def explore_data(data):
    display(data.head())
    display(data.describe())
    display(data.info())
    display(data.columns)

df = get_data()
df.fillna(0, inplace=True)
# Replace all values in time_month with the number that is 1 less than the value
df['time_month '] = (df['time_month '] + 9)%12
explore_data(df)

# Method that returns a dataframe containing all the rows that contain the maximum value of the specified column
def get_max_column_df(data, column_name):
    max_year = data[column_name].max()
    max_year_df = data[data[column_name] == max_year]
    return max_year_df

def get_max_time_df():
    max_year_df = get_max_column_df(df, 'time_year ')
    max_time_df = get_max_column_df(max_year_df, 'time_month ')
    return max_time_df

# Method that returns a list containing the number of rows for each value in the column 'cohort'
def get_cohort_sizes():
    cohort_sizes = df.groupby('cohort ').size()
    return cohort_sizes.values.tolist()
print(get_cohort_sizes())

def get_customer_base_sizes():
    customer_base_sizes = df.groupby('time_month ').size()
    return customer_base_sizes.values.tolist()

#updated from main.py: 

def get_retention_rates(index : int):
    customers_left = df[df['cohort '] == index].groupby('time_month ').size().values.tolist()
    retention_rates = []
    #Putting zeros where retention rates are N/A
    for i in range(1,len(customers_left)):
        retention_rates +=[customers_left[i]/customers_left[i-1]] 
    if index <10: 
        retention_rates += [0]
    retention_rates = retention_rates + [np.NaN]*(12 -len(retention_rates))
    return retention_rates

def get_avg_retention_rate(index : int):
    retention_rates = np.array(get_retention_rates(index))
    return np.nanmean(retention_rates)

