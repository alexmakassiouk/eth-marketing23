import pandas as pd
from pandas import DataFrame

# Import data from data.csv with pandas
def get_raw_data() -> DataFrame:
    data = pd.read_csv('./data.csv', sep=';')
    return data

# Explore data from get_data()
def explore_data(data: DataFrame) -> None:
    print(data.head())
    print(data.describe())
    print(data.info())
    print(data.columns)

# Fill all NaN values with 0
def clean_data(data: DataFrame) -> DataFrame:
    data.fillna(0, inplace=True)
    return data

def modify_month_values(data: DataFrame) -> None:
    data['time_month '] = data['time_month '].apply(lambda x: x - 1)
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

# Method that returns a list containing the number of rows for each value in the column 'cohort'
def get_cohort_sizes(data: DataFrame) -> list[int]:
    cohort_sizes = data.groupby('cohort ').size()
    return cohort_sizes.values.tolist()

def main():
    data = get_data()
    print(get_max_time_df(data))
    print(get_cohort_sizes(data))

main()