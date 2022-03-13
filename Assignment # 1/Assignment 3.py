#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


data = pd.read_csv("netflix_titles.csv")


# In[3]:


data.head()


# In[4]:


data[["cast","director","country"]] = data[["cast","director","country"]].replace(np.nan, "None")
data


# #### Assignment 3

# In[5]:


def set_cast(val):
    if val == "None":
        return 0
    else:
        return len(str(val).split(", "))


# In[6]:


data["cast"].isnull().sum()


# In[7]:


data["num_of_cast"] = data["cast"].apply(set_cast)
data


# In[ ]:




