import pandas as pd

df = pd.read_csv("data/Google_Stock_Price.csv")
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)
df.sort_index(inplace=True)

df = df[['close', 'adjclose', 'volume']]
df = df.resample('M').mean() 
