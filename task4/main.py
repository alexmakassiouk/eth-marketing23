import pandas as pd
from pandas import DataFrame
from IPython.display import display
import numpy as np
DECIMAL_POINTS = 10

# Import data from data.csv with pandas
def get_raw_data() -> DataFrame:
    data = pd.read_csv('../data.csv', sep=';')
    return data

# Explore data from get_data()
def explore_data(data: DataFrame) -> None:
    display(data.head())
    display(data.describe())
    display(data.info())
    display(data.columns)

# Fill all NaN values with 0
def clean_data(data: DataFrame) -> DataFrame:
    data.fillna(0, inplace=True)
    return data

def modify_month_values(data: DataFrame) -> None:
    data['time_month '] = (data['time_month '] + 9)%12
# Replace all values in time_month with the number that is 1 less than the value, according to CPA instructions

def get_data() -> DataFrame:
    data = get_raw_data()
    data = clean_data(data)
    modify_month_values(data)
    return data

# Method that returns a dataframe containing all the rows that contain the maximum value of the specified column
def get_max_column_df(data: DataFrame, column_name: str) -> DataFrame:
    max_year: str | int = data[column_name].max()
    max_year_df = data[data[column_name] == max_year]
    return max_year_df

# Returns the dataframe with the rows that are in the latest time. That is the time with the highest year and month
def get_max_time_df(data: DataFrame) -> DataFrame:
    max_year_df = get_max_column_df(data, 'time_year ')
    max_time_df = get_max_column_df(max_year_df, 'time_month ')
    return max_time_df

def get_cohort_sizes(data: DataFrame) -> list[int]:
    # Return the number of unique user values for each cohort
    cohort_sizes = data.groupby('cohort ')["user  "].nunique()
    return cohort_sizes

def get_customer_base_sizes(data: DataFrame) -> list[int]:
    customer_base_sizes = data.groupby('time_month ')["user  "].nunique()
    return customer_base_sizes

# TASK 3

def get_unique_users_for_month(data: DataFrame, month: int) -> list[int]:
    # Filter the DataFrame for the given month
    filtered_df = data[data['time_month '] == month]

    # Get unique users
    unique_users = filtered_df['user  '].unique()

    return list(unique_users)

def get_retention_rate(data: DataFrame, month_ended_number: int) -> float:
    continuing_customers = 0
    customer_base_0 = get_unique_users_for_month(data, month_ended_number-1)
    new_customer_base = get_unique_users_for_month(data, month_ended_number)
    
    if len(customer_base_0) == 0:
        return np.NaN
    for i in customer_base_0:
        if i in new_customer_base:
            continuing_customers += 1
    return round(continuing_customers/len(customer_base_0),DECIMAL_POINTS)

def get_all_retention_rates(data: DataFrame) -> list[float]:
    retention_rates = []
    for i in range(0,12):
        retention_rates.append(get_retention_rate(data, i))
    return retention_rates

def get_all_retention_rates_for_cohort(data: DataFrame, cohort_number: int) -> list[float]:
    cohort_data = data[data['cohort '] == cohort_number]
    return get_all_retention_rates(cohort_data)

def get_avg_retention_rate(index : int):
    retention_rates = np.array(get_all_retention_rates(index))
    return np.nanmean(retention_rates)

def main():
    data = get_data()
    for cohort_number in range(12):
        print(get_all_retention_rates_for_cohort(data, cohort_number=cohort_number))
