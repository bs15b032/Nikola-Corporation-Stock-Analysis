#!/usr/bin/env python
# coding: utf-8

# In[22]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
import yfinance as yf


# In[24]:


start = "2018-06-11"
end = '2022-06-29'
nkla = yf.download('NKLA',start,end)
nkla


# In[27]:


nkla['Volume'].plot(label = 'nkla',figsize=(16,8))
plt.title('Volume of Stock traded')
plt.legend()


# In[28]:


nkla['MA50'] = nkla['Open'].rolling(50).mean()
nkla['MA200'] = nkla['Open'].rolling(200).mean()
nkla['Open'].plot(figsize = (15,7))
nkla['MA50'].plot()
nkla['MA200'].plot()


# In[40]:


nkla['returns'] = (nkla['Close']/nkla['Close'].shift(1)) -1


nkla['returns'].hist(bins = 100, label = 'NKLA', alpha = 0.5, figsize = (15,7))

plt.legend()


# In[ ]:





# In[41]:


nkla['Daily_Return_Pct']=(nkla['Adj Close']/nkla['Adj Close'].shift(1))-1
nkla
    


# In[ ]:




