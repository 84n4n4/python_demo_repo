import re

import pandas
from sklearn.datasets import load_iris


def main():
    data = load_iris()
    df = pandas.DataFrame(data.data, columns=data.feature_names)
    df['target'] = data['target']
    df['target_name'] = df['target'].apply(lambda x: str(data['target_names'][x]))
    df_grouped = df.groupby('target_name').mean()
    numbers_dict = df_grouped.to_dict(orient='index')
    numbers_dict = {re.sub('[^A-Za-z]+', '', species + key): value for species, params in numbers_dict.items() for
                    key, value in params.items()}

    with open('numbers.tex', 'w') as fd:
        for key, value in numbers_dict.items():
            fd.write('\\newcommand{\\' + key + '}{' + '{:.2f}'.format(value) + '\\xspace}\n')


if __name__ == '__main__':
    main()
