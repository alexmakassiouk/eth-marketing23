import pandas as pd

# Import data from data.csv with pandas
def get_data():
    data = pd.read_csv('../data.csv', sep=';')
    return data

# Explore data from get_data()
def explore_data(data):
    print(data.head())
    print(data.describe())
    print(data.info())
    print(data.columns)

df = get_data()
df.fillna(0, inplace=True)
# Replace all values in time_month with the number that is 1 less than the value
df['time_month '] = df['time_month '].apply(lambda x: x - 1)
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