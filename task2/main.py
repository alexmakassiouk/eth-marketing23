import pandas as pd
from pandas import DataFrame
from IPython.display import display

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

def main():
    data = get_data()
    print(get_max_time_df(data))
    print(get_cohort_sizes(data))
    print(get_max_time_df(clean_data(get_raw_data())))

# main()


