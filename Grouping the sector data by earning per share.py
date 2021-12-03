import pandas as pd
SP500=pd.read_csv('C:/Users/hamza/OneDrive/Desktop/financials.csv')
print(SP500.info())
by_sector=SP500.groupby(['Sector','Name'])
EPS=by_sector['Earnings/Share'].mean().sort_values(ascending=False)
print(EPS.head(10))
