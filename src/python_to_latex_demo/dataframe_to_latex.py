import pandas
from sklearn.datasets import load_iris


def main():
    data = load_iris()
    df = pandas.DataFrame(data.data, columns=data.feature_names)
    df['target'] = data['target']
    df['target_name'] = df['target'].apply(lambda x: data['target_names'][x])
    df_grouped = df.groupby('target_name').mean()

    latex_table = df_grouped.to_latex(float_format="%.2f", na_rep='-', column_format='lrrr', bold_rows=False)
    with open('species.tex', 'w') as fd:
        fd.write(latex_table)


if __name__ == '__main__':
    main()
