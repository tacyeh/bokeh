
import pandas as pd

from bokeh.charts import HeatMap, bin, output_file, show, vplot
from bokeh.sampledata.autompg import autompg as df
from bokeh.palettes import RdYlGn6
from bokeh.sampledata.unemployment1948 import data

# pandas magic
# df = data[data.columns[:-1]]
# df2 = df.set_index(df[df.columns[0]].astype(str))
# df2.drop(df.columns[0], axis=1, inplace=True)
# df3 = df2.transpose()

# bokeh magic
# hm1 = HeatMap(
#     df3, palette=palette,
#     title="categorical heatmap, pd_input",
#     height=400, width=1000
# )
#
# hm_data = df3.values.T
# hm2 = HeatMap(
#     hm_data, palette=palette, title="Unemployment (Array)",
#     xlabel='Years since 1948', ylabel='Months', height=400, width=1000
# )
#
# simple_df = pd.DataFrame(
#     {'apples':[4,5,8,12,4], 'pears':[6,5,4,8,7], 'bananas':[1,2,4,8,12]},
#     index=['2009', '2010', '2011', '2012', '2013']
# )
# hm3 = HeatMap(
#     simple_df, palette=palette,
#     title="Fruit comsumption per year",
#     height=400, width=1000
# )

hm1 = HeatMap(df, bin(x='mpg', y='displ'))

hm2 = HeatMap(df, bin(x='mpg', y='displ', values='cyl', stat='mean'))

hm3 = HeatMap(df, bin(y='displ', x='mpg', values='cyl', stat='mean'))

#hm2 = HeatMap(df, 'mpg', 'displ', 'cyl', spacing_ratio=0.9)

#hm3 = HeatMap(df, 'mpg', 'displ', 'cyl', palette=RdYlGn6)

#hm4 = HeatMap(df, x='cyl', y='displ', values='mpg')

output_file("heatmap.html")

show(vplot(hm1, hm2, hm3))
