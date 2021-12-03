import pandas as pd
import matplotlib.pyplot as plt
SP500=pd.read_csv('C:/Users/hamza/OneDrive/Desktop/financials.csv')
print(SP500.info())
SP500['market_cap_m']=SP500['Market Cap'].div(1e6)
SP500=SP500.drop('Market Cap',axis=1)
SP500_by_sector=SP500.groupby('Sector')
mcap_by_sector=SP500_by_sector.market_cap_m.mean()
print(mcap_by_sector)
mcap_by_sector.sort_values(ascending=True).plot(kind='barh',title='SP500 Average market cap by sectors')
plt.xlabel('In USD ml')
plt.show()
