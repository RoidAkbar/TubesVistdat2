#!/usr/bin/env python
# coding: utf-8

# **FINAL PROJECT VISDAT**
# 
# Anggota Kelompok:
# 1.   Muhammad Ro'id Akbar Aslami
# 2.   Dhikayla Azizah Putri
# 3.   Ghifari Fazlul Makmur

# In[1]:


# Data handling
import pandas as pd
import numpy as np

# Bokeh libraries
from bokeh.io import output_file, output_notebook
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.layouts import row, column, gridplot
from bokeh.models.widgets import Tabs, Panel
from bokeh.models.tools import HoverTool


# In[2]:


# Baca dataset
df_sm = pd.read_csv('stock_market.csv')


# In[3]:


df_sm.head()


# In[4]:


# Mengubah column Date menjadi datetime
df_sm['Date']= pd.to_datetime(df_sm['Date'])
# df_sm.head()


# In[5]:


# Assign data untuk tiap indeks saham
hangs = df_sm[df_sm['Name'] == 'HANG SENG']
nasd = df_sm[df_sm['Name'] == 'NASDAQ']
nikk = df_sm[df_sm['Name'] == 'NIKKEI']

# Membuat ColumDataSource untuk tiap indeks saham
hangs_new = ColumnDataSource(hangs)
nasd_new = ColumnDataSource(nasd)
nikk_new = ColumnDataSource(nikk)


# In[6]:


# Figure di jupyter notebook
output_notebook()

# Membuat figure
fig = figure(x_axis_type='datetime',
             plot_height=400, plot_width=900,
             title='Perbandingan Pergerakan 3 Saham',
             x_axis_label='Tanggal', y_axis_label='Harga Tutup')

# Plotting indeks saham dalam plot line
hangs_line = fig.line('Date', 'Adj Close', 
         color='blue', legend_label='HANG SENG', 
         source=hangs_new)

nasd_line = fig.line('Date', 'Adj Close', 
         color='green', legend_label='NASDAQ', 
         source=nasd_new)

nikk_line = fig.line('Date', 'Adj Close', 
         color='purple', legend_label='NIKKEI', 
         source=nikk_new)


# In[7]:


# Membuat interaksi

# Tooltip
tooltips = [
            ('Name','@Name'),
            ('Close Price', '@{Adj Close}'),
           ]

# Membuat interaksi hover untuk tiap indeks saham
fig.add_tools(HoverTool(tooltips=tooltips,renderers=[hangs_line]))
fig.add_tools(HoverTool(tooltips=tooltips,renderers=[nasd_line]))
fig.add_tools(HoverTool(tooltips=tooltips,renderers=[nikk_line]))

# Membuat interkasi di legend
fig.legend.location = 'bottom_right'
fig.legend.click_policy="hide"

# Menampilkan figure
# show(fig)

# Untuk tampil di heroku
curdoc().add_root(fig)
output_notebook()


# In[ ]:




