#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install google-cloud-bigquery==1.25.0 --use-feature=2020-resolver')

get_ipython().run_cell_magic('bigquery', 'df', 'SELECT\n  departure_delay,\n  COUNT(1) AS num_flights,\n  APPROX_QUANTILES(arrival_delay, 10) AS arrival_delay_deciles\nFROM\n  `bigquery-samples.airline_ontime_data.flights`\nGROUP BY\n  departure_delay\nHAVING\n  num_flights > 100\nORDER BY\n  departure_delay ASC')

df.head()


# In[3]:


import pandas as pd

percentiles = df['arrival_delay_deciles'].apply(pd.Series)
percentiles.rename(columns = lambda x : '{0}%'.format(x*10), inplace=True)
percentiles.head()


# In[4]:


df = pd.concat([df['departure_delay'], percentiles], axis=1)
df.head()


# In[5]:


df.drop(labels=['0%', '100%'], axis=1, inplace=True)
df.plot(x='departure_delay', xlim=(-30,50), ylim=(-50,50));


# In[ ]:




