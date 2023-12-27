import pandas as pd
from pytrends.request import TrendReq
from matplotlib import pyplot as plt


pytrend = TrendReq()
query = ['dolar']
pytrend.build_payload(query, cat=0, timeframe="today 12-m", geo='AR')
datos = pytrend.interest_over_time()

print(datos)

plt.plot(datos)
plt.show()