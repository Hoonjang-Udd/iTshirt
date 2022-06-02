#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


from bs4 import BeautifulSoup


# In[5]:


page = open("C:/Users/Administrator/Desktop/DataScience-master/data/03. test_first.html",'r').read()
soup = BeautifulSoup(page, 'html.parser')
print(soup.prettify())


# In[6]:


list(soup.children)


# In[7]:


html = list(soup.children)[2]
html


# In[8]:


list(html.children)


# In[9]:


body = list(html.children)[3]
body


# In[10]:


soup.body


# In[12]:


list(body.children)


# In[13]:


len(list(body.children))


# In[14]:


soup.find_all('p')


# In[15]:


soup.find('p')


# In[16]:


soup.find_all('p', class_='outer-text')


# In[17]:


soup.find_all(class_="outer-text")


# In[18]:


soup.find_all(id="first")


# In[19]:


soup.find('p')


# In[20]:


list(soup.children)


# In[21]:


soup.head


# In[22]:


soup.head.next_sibling


# In[23]:


soup.head.previous_sibling


# In[24]:


soup.head.next_sibling.next_sibling


# In[25]:


body.p


# In[26]:


body.p.next_sibling.next_sibling


# In[27]:


for each_tag in soup.find_all('p'):
    print(each_tag.get_text())


# In[28]:


body.get_text()


# In[29]:


links = soup.find_all('a')
links


# In[30]:


for each in links:
    href = each['href']
    text = each.string
    print(text + ' -> ' + href)


# In[31]:


from bs4 import BeautifulSoup 
from urllib.request import Request, urlopen

url_base = 'http://www.chicagomag.com'
url_sub = '/Chicago-Magazine/November-2012/Best-Sandwiches-Chicago/'
url = url_base + url_sub

html = urlopen(url)
soup = BeautifulSoup(html, "html.parser")

soup


# In[32]:


from urllib.request import Request, urlopen

req = Request('http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-Chicago/')
webpage = urlopen(req).read()


# In[34]:


from urllib import request
from urllib.request import Request, urlopen

url = "http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-Chicago/"
request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})
webpage = urlopen(request_site).read()


# In[35]:


html = urlopen(url)
soup = BeautifulSoup(html, "html.parser")

soup


# In[36]:


from urllib import request
from urllib.request import Request, urlopen

url = "http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-Chicago/"
request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})
webpage = urlopen(request_site).read()
webpage


# In[ ]:




