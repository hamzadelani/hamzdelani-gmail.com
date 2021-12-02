#Daily, monthly, and annual returns
import matplotlib.pyplot as plt
from pandas_datareader import DataReader
from datetime import date
start_date=date(2011,11,28)
end_date=date(2021,11,26)
series_code='DJIA'
data_source='fred'
djia=DataReader(series_code,data_source,start_date,end_date).dropna()
djia=djia.rename(columns={'DJIA':'Price'})
print(djia.info())
print(djia.head(10))
djia['Monthly_returns']=djia.Price.pct_change(periods=30).mul(100)
djia['Annual_returns']=djia.Price.pct_change(periods=360).mul(100)
print(djia.tail(20))
djia.plot(subplots=True)
plt.show()





