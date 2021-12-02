import matplotlib.pyplot as plt
from pandas_datareader import DataReader
from datetime import date
amzn=pd.read_csv('C:/Users/hamza/OneDrive/Desktop/AMZN_GOOG_MSFT/AMZN.csv',parse_dates=['Date'],index_col='Date').dropna()
goog=pd.read_csv('C:/Users/hamza/OneDrive/Desktop/AMZN_GOOG_MSFT/GOOG.csv',parse_dates=['Date'],index_col='Date').dropna()
msft=pd.read_csv('C:/Users/hamza/OneDrive/Desktop/AMZN_GOOG_MSFT/MSFT.csv',parse_dates=['Date'],index_col='Date').dropna()
start_date=date(2006,1,3)
series_code='^GSPC'
data_source='yahoo'
SP500=DataReader(series_code,data_source,start_date)
print(amzn.info())
print(goog.info())
print(msft.info())
print(SP500.info())
Closing_prices=pd.concat([amzn['Close'],goog['Close'],msft['Close'],SP500['Close']],axis=1).dropna()
Starting_price=Closing_prices.iloc[0]
print(Starting_price.head())
Normalized_price=Closing_prices.div(Starting_price).mul(100)
Normalized_price.columns=['Amazon','Google','Microsoft','S&P500']
print(Normalized_price.head())
Normalized_price.plot()
plt.xlabel('Years')
plt.ylabel('Stock Growth')
plt.title('Stock prices vs Benchmark')
plt.show()

