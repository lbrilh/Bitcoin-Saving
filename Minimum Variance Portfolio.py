#!/usr/bin/env python
# coding: utf-8

# In[441]:


import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[474]:


df_1 = yf.download("AAPL CAT", interval = "1d", start="2018-01-01", end="2023-04-30")
df_2 = yf.download("GC=F ^GSPC", interval = "1d", start="2018-01-01", end="2023-04-30")
df_3 = yf.download("BTC-USD ETH-USD", interval = "1d", start="2018-01-01", end="2023-04-30")
df_4 = yf.download("BTC-USD ETH-USD GC=F ^GSPC", interval = "1d", start="2018-01-01", end="2023-04-30")


# In[475]:


title_1 = 'AAPL/USD, CAT/USD'
title_2 = 'Gold/USD, S&P500/USD'
title_3 = 'BTC/USD, ETH/USD'
title_4 = 'BTC/USD, ETH/USD, Gold/USD, S&P500/USD'

titles = [title_1, title_2, title_3, title_4]


# In[476]:


df_1 = np.log(1+df_1['Adj Close'].pct_change())
df_2 = np.log(1+df_2['Adj Close'].pct_change())
df_3 = np.log(1+df_3['Adj Close'].pct_change())
df_4 = np.log(1+df_4['Adj Close'].pct_change())

df = [df_1, df_2, df_3, df_4]


# In[477]:


display(df_1.head(3))
display(df_2.head(3))
display(df_3.head(3))
display(df_4.head(3))


# In[478]:


def portfolioreturn(weights):
    return np.dot(data.mean(),weights)*360


# In[479]:


def portfoliostd(weights):
    return (np.dot(np.dot(data.cov(),weights),weights))**(1/2)*np.sqrt(360)


# In[480]:


#Create Random Weight to later find optimal portfolio allocation
def weightscreator(df):
    rand = np.random.random(len(df.columns))
    rand /= rand.sum()
    return rand


# In[481]:


returns = [[],[],[],[]]
stds = [[],[],[],[]]
w = [[],[],[],[]]
k = 0

for data in df:
    for i in range(1000):
        weights = weightscreator(data)
        returns[k].append(portfolioreturn(weights))
        stds[k].append(portfoliostd(weights))
        w[k].append(weights)
    k += 1


# In[484]:


# Plot the returns and stds in 4 diffrent subplots
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(15, 15))
plt.subplots_adjust(hspace=0.25)
fig.suptitle("Efficient Frontiers", fontsize=18, y=0.95)
colors = ['red', 'blue', 'green', 'black']
k = 0

for row in range(0,2):
    for col in range(0,2):
        axs[row][col].scatter(stds[k],returns[k], color=colors[k], alpha=0.5)
        plt.title(titles[k])
        plt.xlabel('Portfolio-SD (σ)')
        plt.ylabel('Portfolio-return')
        k += 1


# In[483]:


# Give back the Asset Allocations (weights) for a minimal variance protfolio

k = 0
while k < 4:
    x = np.where(stds[k] == min(stds[k]))
    print(f'Gewichtung von Portfolio {titles[k]}:', w[k][x[0][0]])
    k += 1


# In[ ]:





# In[ ]:




