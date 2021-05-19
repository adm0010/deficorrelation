import pandas as pd
import os
from pandas.plotting import lag_plot
import numpy as np
import sklearn as sk
from sklearn import preprocessing as pr
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from scipy.signal import correlate
from scipy.stats.mstats import spearmanr
from statsmodels.tsa.stattools import acf, adfuller
from statsmodels.graphics.tsaplots import plot_pacf
print(os.getcwd())
pd.plotting.register_matplotlib_converters()

crypto = {}

crypto['comp'] = pd.read_csv(r'/Users/adamcader/Documents/uniwhalechecker/uniwhale1/comp-data.csv')
crypto['aave'] = pd.read_csv(r'/Users/adamcader/Documents/uniwhalechecker/uniwhale1/aave-data.csv')

# Differencing
for coin in crypto:
    crypto[coin]['CloseDiff'] = crypto[coin]['price'].diff()

for coin in crypto:
    crypto[coin]['ClosePctChg'] = crypto[coin]['price'].pct_change().fillna(0)


cryptoAll = {} # for later on

for coin in crypto:
    cryptoAll[coin] = crypto[coin]
    crypto[coin] = crypto[coin][-200:]

for coin in crypto:
    print(coin, len(crypto[coin]))


#for coin in crypto:
#    plt.plot(crypto[coin]['CloseDiff'], label=coin)
   
#plt.legend(loc=2)
#plt.title('Daily Differenced Closing Prices')
#plt.show()

for coin in crypto:
    plt.plot(crypto[coin]['ClosePctChg'], label=coin)
    
plt.legend(loc=2)
plt.title('Daily Percent Change of Closing Price')
plt.show()
