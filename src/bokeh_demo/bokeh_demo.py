import bokeh.palettes
import pandas
from bokeh.models import HoverTool, ColumnDataSource, CategoricalColorMapper
from bokeh.plotting import figure, show
from sklearn.datasets import load_iris

# output_notebook()


def make_tooltip(columns):
    tooltip = "<div><div>"
    for col in columns:
        tooltip += "<span style='font-size: 14px; color: #224499'>" + col + ": </span><br>"
        tooltip += "<span style='font-size: 14px'>@" + col + " </span><br>"
    tooltip += "</div></div>"
    return tooltip


def main():
    data = load_iris()
    df = pandas.DataFrame(data.data, columns=data.feature_names)
    df['target'] = data['target']
    df['target_name'] = df['target'].apply(lambda x: data['target_names'][x])
    df = df.rename(columns={x: x.replace(' ', '_').replace('(', '').replace(')', '') for x in df.columns})
    datasource = ColumnDataSource(df)

    palette = list(bokeh.palettes.Category10_10)
    palette = palette[:len(df['target_name'].value_counts().index) + 1]
    palette = tuple(palette)
    color_mapping_segment = CategoricalColorMapper(factors=df['target_name'].value_counts().index.to_list(),
                                                   palette=palette)

    plot_figure = figure(
        title='',
        width=1200,
        height=800,
        tools=('pan, wheel_zoom, reset', 'box_zoom')
    )

    tooltips = list(df.columns)

    plot_figure.add_tools(HoverTool(tooltips=make_tooltip(tooltips)))

    plot_figure.scatter(
        'sepal_length_cm',
        'sepal_width_cm',
        source=datasource,
        color=dict(field='target_name', transform=color_mapping_segment),
        line_alpha=0.6,
        fill_alpha=0.6,
        size=8
    )
    show(plot_figure)


if __name__ == "__main__":
    main()
