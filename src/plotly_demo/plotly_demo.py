import pandas
import plotly.express as px
from sklearn.datasets import load_iris


def main():
    data = load_iris()
    df = pandas.DataFrame(data.data, columns=data.feature_names)
    df['target'] = data['target']
    df['target_name'] = df['target'].apply(lambda x: data['target_names'][x])
    df = df.rename(columns={x: x.replace(' ', '_').replace('(', '').replace(')', '') for x in df.columns})

    fig = px.scatter(df, x="sepal_width_cm", y="sepal_length_cm", color="target_name",
                     size='petal_length_cm', hover_data=['petal_width_cm'])
    fig.show()


if __name__ == "__main__":
    main()
