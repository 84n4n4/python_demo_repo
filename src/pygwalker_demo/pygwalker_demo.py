import pandas
import pygwalker as pyg
from sklearn.datasets import load_iris


def main():
    data = load_iris()
    df = pandas.DataFrame(data.data, columns=data.feature_names)
    df['target'] = data['target']
    df['target_name'] = df['target'].apply(lambda x: data['target_names'][x])
    df = df.rename(columns={x: x.replace(' ', '_').replace('(', '').replace(')', '') for x in df.columns})

    pyg.walk(df)


if __name__ == "__main__":
    main()
