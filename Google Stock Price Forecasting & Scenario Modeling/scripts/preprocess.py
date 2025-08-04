import matplotlib.pyplot as plt
from load import df
import pandas as pd


df = pd.read_csv("data/Google_Stock_Price.csv")
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)
df.sort_index(inplace=True)
df = df.resample('ME').mean(numeric_only=True)


# Add returns and volatility
df['returns'] = df['adjclose'].pct_change()
df['volatility'] = df['returns'].rolling(window=3).std()
df.dropna(inplace=True)

df.to_csv("data/preprocessed.csv")