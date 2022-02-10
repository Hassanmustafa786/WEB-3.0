#!/usr/bin/env python
# coding: utf-8

# ### ASSIGNMENT : 2

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv("Pokemon.csv")
data.head(n=15)


# In[5]:


speed_mean = data['Speed'].mean()
speed_mean


# In[6]:


def set_speed(val):
    if val < 68:
        return "Low Speed"
    else:
        return "High Speed"


# In[7]:


data["Speed_high_low"] = data["Speed"].apply(set_speed)
data


# In[9]:


mean_hp = data["HP"].mean()
mean_hp


# In[14]:


def set_hp(val):
    if val > 69:
        return "Full HP"
    else:
        return "Low HP"


# In[15]:


data["HP_High_low"] = data["HP"].apply(set_hp)
data


# In[16]:


data.drop(columns=['High_low_HP'], inplace=True)


# In[17]:


data


# In[ ]:




