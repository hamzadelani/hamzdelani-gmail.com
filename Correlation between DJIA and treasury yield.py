import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import DataReader
from datetime import date
import seaborn as sns
start_date=date(2011,11,28)
end_date=date(2021,11,26)
series_code='DJIA'
series_code_2='DGS10'
data_source='fred'
djia=DataReader(series_code,data_source,start_date,end_date).dropna()
dgs10=DataReader(series_code_2,data_source,start_date,end_date).dropna()
print(djia.info())
print(dgs10.info())
data=pd.concat([djia,dgs10],axis=1)
print(data.head(10))
daily_returns=data.pct_change().bfill()
print(daily_returns.head(10))
sns.jointplot(x='DJIA',y='DGS10',data=daily_returns)
plt.show()
