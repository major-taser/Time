#!/usr/bin/env python
# coding: utf-8

# In[14]:


import  os
from os.path import join
import time


def modification_date(filename):
        t = os.path.getmtime(filename)
        t_1=time.ctime(t)
        return t_1

def creation_date(filename):
        t = os.path.getctime(filename)
        t_1=time.ctime(t)
        return t_1

for root, dirs, files in os.walk("."):
        for name in files:
            print(join(root, name), modification_date(join(root, name)), creation_date(join(root, name)))


# In[13]:


x=modification_date(/Data.csv)
print (x)


# In[ ]:




