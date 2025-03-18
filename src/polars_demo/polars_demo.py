import timeit

import pandas
import polars

from src.anchor import data_dir

CSV_FILE = data_dir() + '/random_dataframe.csv'


def main_pandas():
    df = pandas.read_csv(CSV_FILE, dtype={0: 'str', 1: 'str', 2: 'float32'}, parse_dates=['time'])
    df = df.groupby('id').mean()
    # print(df.head())


def main_polars():
    df = polars.read_csv(CSV_FILE, schema_overrides=[polars.Datetime, polars.String, polars.Float32])
    df = df.group_by('id').mean()
    # print(df.head())


N = 1
if __name__ == "__main__":
    print(f'pandas: {timeit.timeit(main_pandas, number=N) / N}')
    print(f'polars: {timeit.timeit(main_polars, number=N) / N}')
