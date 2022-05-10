#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[2]:


page = requests.get(url="https://en.wikipedia.org/wiki/Web_scraping")
page.status_code


# In[88]:


soup = BeautifulSoup(page.text, "html.parser")
print(soup.prettify)


# In[106]:


for heading in soup.find_all(["h1", "h2", "h3"]):
    print(heading.name + ' ' + heading.text.strip())


# In[127]:


h2_tags = soup.find_all("h2")
print(h2_tags)


# In[158]:


p_tags = soup.find(id="mw-content-text").find_all("p", limit=9)
p_tags


# In[159]:


all_data = {"P Tags":p_tags, "h2 Tags":h2_tags}
print(all_data)


# In[162]:


print(len(h2_tags))
print(len(p_tags))
# for dataframe arrays must all be same length


# In[163]:


df = pd.DataFrame(all_data)
df.to_csv("Scrapped.csv")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




