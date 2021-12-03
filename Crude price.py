import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import DataReader
from datetime import date
Start_date=date(2020,1,1)
end_date=date(2021,11,26)
series_code='DCOILWTICO'
data_source='fred'
crude=DataReader(series_code,data_source,Start_date,end_date).dropna()
print(crude.info())
print(crude.head(5))
r90=crude.rolling(window='90D').mean()
print(r90.info())
r360=crude.rolling(window='360D').mean()
pd.concat([crude,r90,r360],axis=1).plot()
plt.xlabel('Year(Months)')
plt.ylabel('Crude rolling price')
plt.legend(['Crude_price','Crude_price_90D_mean','Crude_price_360D_mean'])
plt.show()
