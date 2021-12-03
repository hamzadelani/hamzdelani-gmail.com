import pandas as pd
import matplotlib.pyplot as plt
google=pd.read_csv('C:/Users/hamza/OneDrive/Desktop/AMZN_GOOG_MSFT/GOOG.csv',parse_dates=['Date'],index_col='Date').dropna()
microsoft=pd.read_csv('C:/Users/hamza/OneDrive/Desktop/AMZN_GOOG_MSFT/MSFT.csv',parse_dates=['Date'],index_col='Date').dropna()
print(google.info())
print(microsoft.info())
closing_prices=pd.concat([google['Close'],microsoft['Close']],axis=1)
investment=1000
returns=closing_prices.pct_change().dropna()
print(returns.head(10))
returns_plus_one=returns+1
Cumulative_returns=returns_plus_one.cumprod()
Cumulative_returns.columns=['Google','Microsoft']
Cumulative_returns.mul(investment).plot()
plt.show()
