import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read data
data_stocks = pd.read_csv("ACWI.csv", index_col=0, parse_dates=True)
data_eth = pd.read_csv("eth-usd-max.csv", index_col=0, parse_dates=True)
data_btc = pd.read_csv("btc-usd-max.csv", index_col=0, parse_dates=True)

stocks = data_stocks.iloc[503:,0]
#print(stocks)
eth = data_eth.iloc[1607:2702, 0]
btc = data_btc.iloc[2437:3532, 0]

# adjust to 252 trading days per year
data = pd.DataFrame(btc.to_numpy(), index=pd.date_range(start="2020-01-01",end="2022-12-30")).join(stocks).dropna()
data.columns = ["BTC", "ACWI"]
eth_1 = pd.DataFrame(eth.to_numpy(), index=pd.date_range(start="2020-01-01",end="2022-12-30"))
eth_1.columns = ["ETH"]
data = data.join(eth_1).dropna()
#print(data["BTC"])

"""
Generate Portfolio if lump sum is paid
"""
# Theoretisch Prozentuale Aufteilungen etwas ungenau
part_stocks = 715/stocks[0]
part_btc = 142.5/btc[0] # 
part_eth = 142.5/eth[0]
allocation1 = np.array([part_btc, part_stocks, part_eth])
allocation3 = np.array([199.5/btc[0], part_stocks, 85.5/eth[0]])
allocation2 = np.array([285/btc[0], part_stocks, 0])
allocation4 = np.array([0/btc[0], part_stocks, 285/eth[0]])

performance = data.multiply(allocation1/1000, axis=1)
acwi = pd.DataFrame(part_stocks*data["ACWI"]/715)
acwi.columns = ["Stock return"]
performance["Stock return"] = acwi - 1
performance["Stock: 70%, BTC: 15%, ETH: 15%"] = performance[["BTC", "ACWI", "ETH"]].sum(axis=1) - 1
performance["Stock: 70%, BTC: 30%"] = data.multiply(allocation2/1000, axis=1).sum(axis=1)-1
performance["Stock: 70%, BTC: 20%, ETH: 10%"] = data.multiply(allocation3/1000, axis=1).sum(axis=1)-1
performance["Stock: 70%, ETH: 30%"] = data.multiply(allocation4/1000, axis=1).sum(axis=1)-1
#print(performance)

"""
Generate DCA-Portfolio: Invest Daily and 12 times a year
"""
#Erstelle Array wie sich crypto anteil entwickelt
#print(np.arange(1,7)*monthly)
ranger = np.array(np.arange(1,7)*142.5/6, )
share = np.zeros((756,4)) #756/6=126
for i in range(0,6):
    share[i*126:(i+1)*126,0]= ((i+1) * 142.5/6)
    share[i*126:(i+1)*126,2]= ((i+1) * 142.5/6)
    share[i*126:(i+1)*126,1]= ((i+1) * 715/6)
    share[i*126:(i+1)*126,3]= ((i+1)*(1000/6))

#print(stocks) # adjust to stocks
asset_owned = np.zeros((6,3))
asset_owned[0,0] = 142.5/6/btc["20200101"]
asset_owned[1,0] = asset_owned[0,0] + 142.5/6/btc["20200601"]
asset_owned[2,0] = asset_owned[1,0] + 142.5/6/btc["20210101"]
asset_owned[3,0] = asset_owned[2,0] + 142.5/6/btc["20210601"]
asset_owned[4,0] = asset_owned[3,0] + 142.5/6/btc["20220101"]
asset_owned[5,0] = asset_owned[4,0] + 142.5/6/btc["20220601"]
asset_owned[0,2] = 142.5/6/eth["20200101"]
asset_owned[1,2] = asset_owned[0,2] + 142.5/6/eth["20200601"]
asset_owned[2,2] = asset_owned[1,2] + 142.5/6/eth["20210101"]
asset_owned[3,2] = asset_owned[2,2] + 142.5/6/eth["20210601"]
asset_owned[4,2] = asset_owned[3,2] + 142.5/6/eth["20220101"]
asset_owned[5,2] = asset_owned[4,2] + 142.5/6/eth["20220601"]
asset_owned[0,1] = 715/6/stocks["2020-01-02"]
asset_owned[1,1] = asset_owned[0,1] + 715/6/stocks["2020-06-01"]
asset_owned[2,1] = asset_owned[1,1] + 715/6/stocks["2021-01-04"]
asset_owned[3,1] = asset_owned[2,1] + 715/6/stocks["2021-06-01"]
asset_owned[4,1] = asset_owned[3,1] + 715/6/stocks["2022-01-03"]
asset_owned[5,1] = asset_owned[4,1] + 715/6/stocks["2022-06-01"]

#print(asset_owned)

# ToDo: Bitcoin anteil über DCA Phase

# print(data["BTC"])
performance_dca = data
#(performance_dca)
performance_dca["20200102":"20200529"] = data["20200102":"20200529"]*asset_owned[0,:]/(142.5/6+142.5/6+715/6)
performance_dca["20200601":"20201231"] = data["20200601":"20201231"]*asset_owned[1,:]/(2*(142.5/6+142.5/6+715/6))
performance_dca["20210101":"20210601"] = data["20210101":"20210601"]*asset_owned[2,:]/(3*(142.5/6+142.5/6+715/6))
performance_dca["20210602":"20211231"] = data["20210602":"20211231"]*asset_owned[3,:]/(4*(142.5/6+142.5/6+715/6))
performance_dca["20220103":"20220601"] = data["20220103":"20220601"]*asset_owned[4,:]/(5*(142.5/6+142.5/6+715/6))
performance_dca["20220602":"20221230"] = data["20220602":"20221230"]*asset_owned[5,:]/(6*(142.5/6+142.5/6+715/6))

#print(performance_dca)
performance_dca = performance_dca.sum(axis=1)-1
performance["DCA Portfolio"] = performance_dca

#print(performance)

ax = performance[["Stock: 70%, BTC: 15%, ETH: 15%", "Stock: 70%, BTC: 30%", "Stock: 70%, BTC: 20%, ETH: 10%", "Stock: 70%, ETH: 30%", "DCA Portfolio", "Stock return"]].plot()
ax.tick_params(axis='both', labelsize=14)
ax.set_ylabel("Return in 100%", fontsize = 20)
ax.set_xlabel("Date", fontsize=20)
ax.set_title("Comparing Portfolio Returns", fontsize = 30)
plt.show()

performance.to_csv("Portfolio Performance")