import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Correlation Bitcoin und Ethereum

data_tsla = pd.read_csv("TSLA.csv", index_col=0, parse_dates=True)
data_eth = pd.read_csv("eth-usd-max.csv", index_col=0, parse_dates=True)
data_btc = pd.read_csv("btc-usd-max.csv", index_col=0, parse_dates=True)
data_nasdaq = pd.read_csv("NASDAQ.csv", index_col=0, parse_dates=True)

# print(data_eth.drop(["market_cap", "total_volume"], axis = 1).head)
dates = pd.date_range(start="2020-01-01",end="2022-12-31", periods=1209)

nasdaq = data_nasdaq.iloc[:,0]
tsla = data_tsla.iloc[:, 0]
eth = data_eth.iloc[877:2702, 0]
btc = data_btc.iloc[1707:3532, 0]



#fig = plt.figure()
#plt.subplot(1,2,1)
#plt.plot(dates, eth, dates, btc)
#plt.subplot(1,2,2)
#plt.plot(tsla)

#plt.show()

# plot correlation


corr_btc_tsla = pd.DataFrame(btc.to_numpy(), index=pd.date_range(start="2018-01-01",end="2022-12-30")).join(tsla).dropna()
corr_eth_tsla = pd.DataFrame(eth.to_numpy(), index=pd.date_range(start="2018-01-01",end="2022-12-30")).join(tsla).dropna()

corr_btc_nasdaq = pd.DataFrame(btc.to_numpy(), index=pd.date_range(start="2018-01-01",end="2022-12-30")).join(nasdaq).dropna()
corr_eth_nasdaq = pd.DataFrame(eth.to_numpy(), index=pd.date_range(start="2018-01-01",end="2022-12-30")).join(nasdaq).dropna()
#print(corr_btc_nasdaq)


np_corr_btc_tsla = corr_btc_tsla.to_numpy()
np_corr_eth_tsla = corr_eth_tsla.to_numpy()

np_corr_btc_nasdaq = corr_btc_nasdaq.to_numpy()
np_corr_eth_nasdaq = corr_eth_nasdaq.to_numpy()


np_btc_tsla = []
np_eth_tsla = []
np_btc_nasdaq = []
np_eth_nasdaq = []

k = 0

for j in (np_corr_btc_tsla, np_corr_eth_tsla, np_corr_btc_nasdaq, np_corr_eth_nasdaq):
    for i in range(0,j.shape[0]-40):        
        if k == 0:
            np_btc_tsla.append(np.corrcoef(j[i:i+40,0],j[i:i+40,1], rowvar=False)[0,1])
        if k == 1:
            np_eth_tsla.append(np.corrcoef(j[i:i+40,0],j[i:i+40,1], rowvar=False)[0,1])
        if k == 2:
            np_btc_nasdaq.append(np.corrcoef(j[i:i+40,0],j[i:i+40,1], rowvar=False)[0,1])
        if k == 3:
            np_eth_nasdaq.append(np.corrcoef(j[i:i+40,0],j[i:i+40,1], rowvar=False)[0,1])
    k += 1

corr = pd.DataFrame(np.array(np_btc_nasdaq), index=pd.date_range(start="2018-01-01",end="2022-12-30", periods=1219))
corr.columns = ["BTC-NASDAQ"]
ax = corr.plot(legend=False, style = {"BTC-NASDAQ": "*:k"})
ax.tick_params(axis='both', labelsize=14)
ax.set_ylabel("40-Day Correlation", fontsize = 20)
ax.set_xlabel("Date", fontsize=20)
ax.set_title("40-Day Correlation BTC-NASDAQ", fontsize = 30)

corr = pd.DataFrame(np.array(np_eth_nasdaq), index=pd.date_range(start="2018-01-01",end="2022-12-30", periods=1219))
corr.columns = ["ETH-NASDAQ"]
ax = corr.plot(legend=False, style = {"ETH-NASDAQ": "*:k"})
ax.tick_params(axis='both', labelsize=14)
ax.set_ylabel("40-Day Correlation", fontsize = 20)
ax.set_xlabel("Date", fontsize=20)
ax.set_title("40-Day Correlation ETH-NASDAQ", fontsize = 30)

corr = pd.DataFrame(np.array(np_btc_tsla), index=pd.date_range(start="2018-01-01",end="2022-12-30", periods=1219))
corr.columns = ["BTC-TESLA"]
ax = corr.plot(legend=False, style = {"BTC-TESLA": "*:k"})
ax.tick_params(axis='both', labelsize=14)
ax.set_ylabel("40-Day Correlation", fontsize = 20)
ax.set_xlabel("Date", fontsize=20)
ax.set_title("40-Day Correlation BTC-TESLA", fontsize = 30)

corr = pd.DataFrame(np.array(np_eth_tsla), index=pd.date_range(start="2018-01-01",end="2022-12-30", periods=1219))
corr.columns = ["ETH-TESLA"]
ax = corr.plot(legend=False, style = {"ETH-TESLA": "*:k"})
ax.tick_params(axis='both', labelsize=14)
ax.set_ylabel("40-Day Correlation", fontsize = 20)
ax.set_xlabel("Date", fontsize=20)
ax.set_title("40-Day Correlation ETH-TESLA", fontsize = 30)








eth = pd.DataFrame(eth.to_numpy(), index=pd.date_range(start="2018-01-01",end="2022-12-30"))
eth.columns = ["ETH"]
print(eth)
btc = pd.DataFrame(btc.to_numpy(), index=pd.date_range(start="2018-01-01",end="2022-12-30"))
btc = btc.join(nasdaq)
btc.columns = ["BTC", "NASDAQ"]


daily_simple_return = btc.pct_change(1) 
daily_simple_return.dropna(inplace=True)

#print(daily_simple_return.head)

print('Daily simple returns')
ax = daily_simple_return.plot()
ax.tick_params(axis='both', labelsize=14)
ax.set_ylabel("Daily simple returns", fontsize = 20)
ax.set_xlabel("Date", fontsize=20)
ax.set_title("Volatility in Daily simple returns", fontsize = 30)
#plt.show()

# Return PER UNIT OF RISK- Sharpe Ratio
print('Annualized Standard Deviation (Volatality(%), 252 trading days) of individual assets in your portfolio on the basis of daily simple returns') # ????????
Avg_daily = daily_simple_return.mean()
print(Avg_daily / (daily_simple_return.std() * np.sqrt(252)) *100)

# comparing developement of BTC, ETH, NASDAQ
all_assets = btc.join(eth)
all_assets = all_assets.pct_change(1).dropna()
daily_cummulative_simple_return =(all_assets+1).cumprod()




eth = pd.DataFrame(eth.to_numpy(), index=pd.date_range(start="2018-01-01",end="2022-12-30"))
eth.columns = ["ETH"]
btc = data_btc.iloc[1707:3532, 0]
btc = pd.DataFrame(btc.to_numpy(), index=pd.date_range(start="2018-01-01",end="2022-12-30"))
btc.columns = ["BTC"]
btc = btc.join(eth)
np_corr_btc_eth = btc.to_numpy() 
np_btc_eth = []

for i in range(0,np_corr_btc_eth.shape[0]-40):        
    np_btc_eth.append(np.corrcoef(np_corr_btc_eth[i:i+40,0],np_corr_btc_eth[i:i+40,1], rowvar=False)[0,1])

corr = pd.DataFrame(np.array(np_btc_eth), index=pd.date_range(start="2018-01-01",end="2022-12-30", periods=1785))
corr.columns = ["BTC-ETH"]
ax = corr.plot(legend=False, style = {"BTC-ETH": "*:k"})
ax.tick_params(axis='both', labelsize=14)
ax.set_ylabel("40-Day Correlation", fontsize = 20)
ax.set_xlabel("Date", fontsize=20)
ax.set_title("40-Day Correlation BTC-ETH", fontsize = 30)








#print(daily_simple_return.head)
ax = daily_cummulative_simple_return.plot()
ax.tick_params(axis='both', labelsize=14)
ax.set_ylabel("Growth of USD 1 Investment", fontsize = 20)
ax.set_xlabel("Date", fontsize=20)
ax.set_title("Daily Cummulative Simple returns/growth of investment", fontsize = 30)
plt.show()