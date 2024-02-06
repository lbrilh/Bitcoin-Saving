# Portfolio Performance and Correlation Analysis

This repository contains two Python scripts for analyzing portfolio performance and correlation between different assets. Here's a brief overview of each script and how to use them:

## portfolio_performance.py

This script is used for analyzing the performance of a portfolio consisting of Bitcoin (BTC), a global stock market index (ACWI), and Ethereum (ETH). It calculates and compares the returns of different portfolio allocations and a Dollar-Cost Averaging (DCA) strategy. Here are the main functionalities:

### Data Loading

- It loads historical price data for BTC, ACWI, and ETH from CSV files.
- The data is then trimmed to a specific date range (2020-01-01 to 2022-12-30) to match the analysis period.

### Portfolio Allocation

- It defines various portfolio allocations, such as "Stock: 70%, BTC: 15%, ETH: 15%", and calculates their performance.
- Theoretical percentage allocations are used for these portfolios.

### Dollar-Cost Averaging (DCA) Portfolio

- It simulates a DCA strategy by investing daily and rebalancing the portfolio 12 times a year.
- Asset ownership and allocation are calculated over time for BTC, ACWI, and ETH.

### Results and Visualization

- The script calculates and visualizes the performance of different portfolios, including the DCA portfolio, using Matplotlib.
- The resulting portfolio performance is saved as a CSV file named "Portfolio Performance."

## Minimum Variance Portfolio.py

This script focuses on constructing an efficient portfolio based on historical returns and volatility. It uses Yahoo Finance data for assets like Apple (AAPL), Caterpillar (CAT), Gold (GC=F), and the S&P 500 index (^GSPC) from 2018-01-01 to 2023-04-30. Here's what this script does:

### Data Retrieval

- It uses the Yahoo Finance API (yfinance) to download historical price data for the specified assets.

### Efficient Frontier

- It calculates the returns and standard deviations (volatility) of portfolios with randomly generated asset weightings.
- The script generates 1,000 portfolios for each asset combination and stores the returns, standard deviations, and weights.

### Efficient Frontier Visualization

- The script plots the efficient frontier for each asset combination, showing the trade-off between risk (standard deviation) and return.

### Minimum Variance Portfolio

- It identifies the portfolio with the minimum standard deviation (volatility), which represents the least risky portfolio.
- The weights of the assets in this minimum variance portfolio are displayed.

## Correlation_BTC_ETH_Tesla.py

This script analyzes the correlation between Bitcoin (BTC) and Ethereum (ETH), as well as between Bitcoin and Tesla (TSLA), over a 40-day rolling window. It also includes the correlation of Bitcoin with the NASDAQ index. Here's what this script does:

### Data Loading

- It loads historical price data for TSLA, ETH, BTC, and NASDAQ from CSV files.
- The data is then trimmed to a specific date range (2020-01-01 to 2022-12-30) to match the analysis period.

### Correlation Calculation

- It calculates the 40-day rolling correlation between BTC and ETH, BTC and TSLA, and BTC and NASDAQ.
- The correlation values are computed and stored over time.

### Results and Visualization

- The script visualizes the 40-day rolling correlations between the specified asset pairs using Matplotlib.

## Instructions for Use

1. Ensure you have the required libraries (pandas, numpy, matplotlib, yfinance) installed in your Python environment.
2. Place the necessary CSV data files ("ACWI.csv," "eth-usd-max.csv," "btc-usd-max.csv," "TSLA.csv," "NASDAQ.csv") in the same directory as the scripts.
3. Run each script to perform the desired analysis.
4. Review the generated visualizations and output to gain insights into portfolio performance and asset correlations.

Feel free to customize the analysis parameters or extend the functionality of these scripts to suit your specific needs.
