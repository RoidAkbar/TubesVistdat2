# -*- coding: utf-8 -*-
"""backupcovid.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bZF6fCsntgQKkjiqJIPVMmIzxYD1pYlR
"""

# Data handling
import pandas as pd
import numpy as np
import bokeh

# Bokeh libraries
from bokeh.io import output_file, output_notebook
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.layouts import row, column, gridplot
from bokeh.models.widgets import Tabs, Panel
from bokeh.io import show,curdoc
# Baca dataset
df_sm = pd.read_csv('covid.csv')

df_sm.head()

# Mengubah column Date menjadi datetime
df_sm['Date']= pd.to_datetime(df_sm['Date'])
# df_sm.head()

# Assign data untuk tiap data covid
jkt = df_sm[df_sm['Province'] == 'DKI JAKARTA']
jabar= df_sm[df_sm['Province'] == 'JAWA BARAT']
banten = df_sm[df_sm['Province'] == 'BANTEN']

# Membuat ColumDataSource untuk tiap provinsi
jkt_new = ColumnDataSource(jkt)
jabar_new = ColumnDataSource(jabar)
banten_new = ColumnDataSource(banten)

# Membuat figure
fig = figure(x_axis_type='datetime',
             plot_height=400, plot_width=900,
             title='Data Covid',
             x_axis_label='Tanggal', y_axis_label='Jumlah')
# Render indeks covid dalam plot line
jkt_line = fig.line('Date', 'Daily_Case', 
         color='blue', legend_label='DKI JAKARTA', 
         source=jkt_new)

jabar_line = fig.line('Date', 'Daily_Case', 
         color='green', legend_label='JAWA BARAT', 
         source=jabar_new)

banten_line = fig.line('Date', 'Daily_Case', 
         color='purple', legend_label='BANTEN', 
         source=banten_new)

# Membuat interaksi
from bokeh.models.tools import HoverTool

# Tooltip
tooltips = [
            ('Provinsi','@Province'),
            ('Jumlah Kasus', '@{Daily_Case}'),
           ]

# Membuat interaksi hover untuk tiap indeks covid
fig.add_tools(HoverTool(tooltips=tooltips,renderers=[jkt_line]))
fig.add_tools(HoverTool(tooltips=tooltips,renderers=[jabar_line]))
fig.add_tools(HoverTool(tooltips=tooltips,renderers=[banten_line]))

# Membuat interkasi di legend
fig.legend.location = 'top_right'
fig.legend.click_policy="hide"

# Menampilkan figure
curdoc().add_root(fig)
output_notebook()
