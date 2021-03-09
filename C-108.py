import plotly.figure_factory as ff
import pandas as pd
import csv

df=pd.read_csv('data.csv')
weightlist=df['Weight(Pounds)'].tolist()
print(weightlist)
fig=ff.create_distplot([weightlist],['Weight'],show_hist=False)

fig.show()