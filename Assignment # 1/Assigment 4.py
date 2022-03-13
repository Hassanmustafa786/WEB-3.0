#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


data = pd.read_csv("netflix_titles.csv")
data.head()


# #### Q1: In the netflix dataset replace all null values present in country column with united states.

# In[16]:


data.replace(to_replace = np.nan, value = "United States", inplace = True)
data


# In[17]:


data.head()


# #### Q2: Show 10 countries with most tv-shows and movies

# In[86]:


section = data.groupby("type")["country"].value_counts()
print(section['Movie'].head(10))
print(section['TV Show'].head(10))


# In[87]:


data.type.value_counts()


# #### Q3: Count of movies released in year respective years.

# In[113]:


section1 = data.groupby("type")["release_year"].value_counts()
print(section1["Movie"])


# #### Q4: Similarly, count of tv-shows released in there respective years.

# In[114]:


section2 = data.groupby("type")["release_year"].value_counts()
print(section2["TV Show"])


# In[ ]:





# In[ ]:




