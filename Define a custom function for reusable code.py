#creating a custom code for its reusability
import matplotlib.pyplot as plt
import pandas as pd
def plot_timeseries(axes,x,y, color, xlabel, ylabel):
    axes.plot(x,y, color=color)
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel,color=color)
fig,ax=plt.subplots()
amzn=pd.read_csv('C:/Users/hamza/OneDrive/Desktop/AMZN_GOOG_MSFT/AMZN.csv',parse_dates=['Date'],index_col='Date').dropna()
print(amzn.info())
closing_price=amzn['Close']
plot_timeseries(ax,amzn.index,closing_price,'red','Time (years)','Closing price of amazon')
plt.show()
