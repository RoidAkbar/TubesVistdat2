#!/usr/bin/env python
# coding: utf-8

# In[374]:


import pandas as pd
import numpy as np
import bokeh


# In[375]:


# Bokeh libraries
from bokeh.io import output_file, output_notebook
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.layouts import row, column, gridplot
from bokeh.models.widgets import Tabs, Panel
from bokeh.io import show,curdoc


# In[360]:


# Baca dataset
df_cvd = pd.read_csv('covid_2021.csv')


# In[361]:


df_cvd.head()


# In[362]:


# df_cvd.set_index('Date', inplace=True)
# df_cvd.head()


# In[363]:


# Mengubah column Date menjadi datetime
df_cvd['Date']= pd.to_datetime(df_cvd['Date'])


# In[364]:


# Assign data untuk tiap data covid
jkt = df_cvd[df_cvd['Province'] == 'DKI JAKARTA']
jabar= df_cvd[df_cvd['Province'] == 'JAWA BARAT']
jatim = df_cvd[df_cvd['Province'] == 'JAWA TIMUR']


# In[365]:


# Membuat ColumDataSource untuk tiap provinsi
jkt_new = ColumnDataSource(jkt)
jabar_new = ColumnDataSource(jabar)
jatim_new = ColumnDataSource(jatim)


# In[366]:


# Membuat figure
fig = figure(x_axis_type='datetime',
             plot_height=400, plot_width=900,
             title='Data Covid',
             x_axis_label='Tanggal', y_axis_label='Jumlah')


# In[367]:


# Render indeks covid dalam plot line
jkt_line = fig.circle('Date', 'Daily_Case', 
         size=10, alpha=0.5, color='blue', legend_label='DKI JAKARTA', 
         source=jkt_new)
jabar_line = fig.circle('Date', 'Daily_Case', 
         size=10, alpha=0.5, color='green', legend_label='JAWA BARAT', 
         source=jabar_new)

jatim_line = fig.circle('Date', 'Daily_Case', 
         size=10, alpha=0.5, color='purple', legend_label='JAWA TIMUR', 
         source=jatim_new)


# In[368]:


# Membuat interaksi
from bokeh.models.tools import HoverTool


# In[369]:


# Tooltip
tooltips = [
            ('Case','@{Daily_Case}'),
            ('Recovered','@{Daily_Recovered}'),
            ('Death', '@{Daily_Death}'),
           ]


# In[370]:


# Membuat interaksi hover untuk tiap indeks covid
fig.add_tools(HoverTool(tooltips=tooltips,renderers=[jkt_line]))
fig.add_tools(HoverTool(tooltips=tooltips,renderers=[jabar_line]))
fig.add_tools(HoverTool(tooltips=tooltips,renderers=[jatim_line]))


# In[371]:


# Membuat interkasi di legend
fig.legend.location = 'top_right'
fig.legend.click_policy="hide"


# In[372]:


# Menampilkan figure
curdoc().add_root(fig)
output_notebook()
# show(fig)


# In[ ]:




