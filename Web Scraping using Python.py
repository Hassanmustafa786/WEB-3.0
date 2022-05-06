#!/usr/bin/env python
# coding: utf-8

# In[9]:


pip install requests


# In[10]:


pip install bs4


# In[11]:


pip install html5lib


# In[15]:


import requests
from bs4 import BeautifulSoup
url = "https://www.dsu.edu.pk/"
r = requests.get(url)


# In[20]:


html_Content = r.content
#print(html.Content)


# In[21]:


soup = BeautifulSoup(html_Content, 'html.parser')
#print(soup.prettify)


# In[54]:


title = soup.title
print(type(soup))              # 1.BeautifulSoup
print(type(title))             # 2.Tag
print(type(title.string))      # 3.NavigableString
# 4. Comment
markup = "<p><!-- this is a comment --></p>"
soup2 = BeautifulSoup(markup)
print(type(soup2.p.string))


# In[47]:


paragraphs = soup.find_all('p')
#print(paragraphs)


# In[52]:


anchors = soup.find_all('a')
all_links = set()
#print(anchors)
# Get all the links on the page
for link in anchors:
    if(link.get('href') != '#'):
        linkText = "https://www.dsu.edu.pk/" + link.get('href')
        all_links.add(linkText)
        print(linkText)


# In[35]:


print(soup.find('p'))


# In[45]:


print(soup.find('p').get_text())
print(soup.get_text())


# In[ ]:




