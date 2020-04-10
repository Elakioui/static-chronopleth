import numpy as np
import pandas as pd
import plotly as py
import plotly.express as ex
import plotly.graph_objs as go


from plotly.subplots import make_subplots
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)

#read Data
df = pd.read_csv('covid_19_data.csv')


#Rename columns
df = df.rename(columns={'Country/Region':'Country'})
df = df.rename(columns={'ObservationDate':'Date'})

#Manipulate the original dataframe
df_countries = df.groupby(
    ['Country', 'Date']
    ).sum().reset_index().sort_values('Date', ascending = False)

df_countries = df_countries.drop_duplicates(subset = ['Country'])
df_countries = df_countries[df_countries['Confirmed']>0]
print(df_countries)