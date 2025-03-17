from datetime import datetime

import pandas
import numpy as np

from src.anchor import data_dir


def main():
    size = int(10e6)
    index = pandas.date_range(start=datetime(year=2000, month=1, day=1), periods=size, freq='30s')
    index.name = 'time'
    ids = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    df = pandas.DataFrame(index=index, data={
        'id': np.random.randint(0, len(ids), size),
        'value': np.random.random(size)
    })
    df['id'] = df['id'].apply(lambda x: ids[x])
    df.to_csv(data_dir() + '/random_dataframe.csv')



if __name__ == '__main__':
    main()