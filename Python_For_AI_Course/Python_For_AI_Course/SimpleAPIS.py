import pandas as pd

a= {'x':[4,9,8,20], 'y':[8,6,2,7]}
dt=pd.DataFrame(a) #x and y should have the same length
print(dt)
print(dt.mean())

from pycoingecko import CoinGeckoAPI
cg= CoinGeckoAPI()
bitcoin_data= cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=30)
print(bitcoin_data)
print(bitcoin_data['prices'][0:8])

#converting a json to dataframe
data= pd.DataFrame(bitcoin_data['prices'], columns=['TimeStamp', 'Price'])
print(data.head())
#add a new column
data['Date']=pd.to_datetime(data['TimeStamp'], unit='ms')

print(data.head())

#new dataframe grouped by date
candlestick_data=data.groupby(data.Date.dt.date).agg({'Price':['min','max','first','last']})

print(candlestick_data.head())


