#!/usr/bin/env python
# coding: utf-8

# In[13]:


def solve (n=1000):
    soucet = 0
    for i in range (1, n):
        if (i% 3 == 0) or (i%5 ==0):
            soucet += i
    return soucet
          
        
print(solve())    


# In[ ]:




