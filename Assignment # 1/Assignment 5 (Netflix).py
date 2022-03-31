#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


df = pd.read_csv("netflixData.csv")
df.head()


# In[4]:


df.groupby("Content Type")["Production Country"].value_counts(ascending = False)


# In[5]:


sns.heatmap(df.isnull())


# In[6]:


df[["Production Country","Director","Cast","Release Date","Rating","Duration","Imdb Score","Date Added"]].replace(np.nan, "None", inplace=True)


# In[7]:


df.isnull().sum()


# In[21]:


plt.figure(figsize=(25,10))
sort = df["Production Country"].value_counts(ascending = True)
sns.countplot(x= sort, data = df)


# In[9]:


sns.countplot(x="Content Type", data=df)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




