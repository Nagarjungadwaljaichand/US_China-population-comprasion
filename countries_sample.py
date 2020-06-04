#!/usr/bin/env python
# coding: utf-8

# In[29]:


import pandas as pd
import matplotlib.pyplot as plt 


# In[11]:


data=pd.read_csv('Desktop/PRedictive Analytics/countries.csv')


# In[25]:


data


# In[37]:


US = data [data.country == 'United States']
US


# In[36]:


china = data [data. country == 'China']
china


# In[48]:


US.population/ US.population.iloc[0]*100
china.population/ china.population.iloc[0]*100


# In[57]:


plt.plot(US.year, US.population/ US.population.iloc[0] *100)
plt.plot(china.year, china.population/ china.population.iloc[0] *100)
plt.legend(['USA','China'])
plt.xlabel('Year')
plt.ylabel('Population')
plt.show()


# In[ ]:




