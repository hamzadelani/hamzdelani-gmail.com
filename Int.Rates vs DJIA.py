import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import DataReader
from datetime import date
start_date=date(2011,11,27)
end_date=date(2021,11,26)
series_code='DGS10'
data_source='fred'
interest_rate=DataReader(series_code,data_source,start_date,end_date)
data_source_2='yahoo'
djia=DataReader('^DJI',data_source_2,start_date,end_date)
interrelation=pd.concat([djia['Close'],interest_rate],axis=1)
print(interrelation.info())
print(interrelation.head())
interrelation.columns=['DJIA','Interest Rate']
interrelation.plot(secondary_y='Interest Rate')
plt.show()
