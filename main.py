#Comparing Amazon and google cumulative returns
import pandas as pd
import matplotlib.pyplot as plt
google=pd.read_csv('C:/Users/hamza/OneDrive/Desktop/AMZN_GOOG_MSFT/GOOG.csv',parse_dates=['Date'],index_col='Date').dropna()
microsoft=pd.read_csv('C:/Users/hamza/OneDrive/Desktop/AMZN_GOOG_MSFT/MSFT.csv',parse_dates=['Date'],index_col='Date').dropna()
print(google.info())
print(microsoft.info())
closing_prices=pd.concat([google['Close'],microsoft['Close']],axis=1)
starting_price=closing_prices.iloc[0]
Normalized_price=closing_prices.div(starting_price).mul(100)
Normalized_price.columns=['Google','Microsoft']
print(Normalized_price.head())
Normalized_price.plot()
plt.xlabel('Years')
plt.ylabel('Returns on both stocks')
plt.title('Google vs Microsoft stock prices')
plt.show()



