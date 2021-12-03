import pandas as pd
import matplotlib.pyplot as plt
amzn=pd.read_csv('C:/Users/hamza/OneDrive/Desktop/AMZN_GOOG_MSFT/AMZN.csv',parse_dates=['Date'],index_col='Date').dropna()
print(amzn.info())
Closing_price=amzn['Close']
rolling_90D=amzn['Close'].rolling(window='90D').mean()
print(rolling_90D.head(5))
rolling_360D=amzn['Close'].rolling(window='360D').mean()
print(rolling_360D.head(5))
pd.concat([Closing_price,rolling_90D,rolling_360D],axis=1).dropna().plot()
plt.xlabel('Years')
plt.ylabel('Closing_price (90D & 360D)')
plt.legend(['Close','Close_mean_90D','Close_mean_360D'])
plt.show()
