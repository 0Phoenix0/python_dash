import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file form Datasets folder
df = pd.read_csv('../Datasets/CoronaTimeSeries.csv')

# Preparing data
data = [go.Heatmap(x=df['Day'],
                   y=df['WeekofMonth'],
                   z=df['Recovered'],
                   colorscale='jet')]

# Preparing Layout
layout = go.Layout(title='Corona Virus Recovered Cases',
                   xaxis_title="Day of Week",
                   yaxis_title="Week of Month")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='heatmap.html')