#!/usr/bin/env python
# coding: utf-8

# In[66]:


get_ipython().system('pip install autoscraper')


# In[67]:


from autoscraper import AutoScraper


# In[68]:


flipkart_url="https://www.flipkart.com/search?q=handsfree&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
wanted_list=["₹369","Aroma NB120 Tehalka - 28 Hours Playtime Bluetooth Neckb...","3.9"]


# In[69]:


scraper = AutoScraper()
result = scraper.build(flipkart_url , wanted_list)
print(result)


# In[70]:


scraper.get_result_similar(flipkart_url, grouped =True)


# In[81]:


scraper.set_rule_aliases({'rule_2ry7':'Title','rule_utzo':'Price'})
scraper.keep_rules(['rule_2ry7','rule_utzo'])
scraper.save('amazon-search')


# In[87]:


results = scraper.get_result_similar('https://www.flipkart.com/search?q=shoes&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off', group_by_alias = True)


# In[88]:


results['Title']


# In[80]:


results['Price']


# In[ ]:




