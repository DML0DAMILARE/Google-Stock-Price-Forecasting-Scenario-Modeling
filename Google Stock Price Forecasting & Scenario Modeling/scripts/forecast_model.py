from prophet import Prophet
from load import df

prophet_df = df.reset_index()[['date', 'adjclose']]
prophet_df.columns = ['ds', 'y']

model = Prophet()
model.fit(prophet_df)

future = model.make_future_dataframe(periods=36, freq='M')  # 3 years ahead
forecast = model.predict(future)

forecast[['ds', 'yhat']].tail()
forecast.to_excel("outputs/forecast_base.xlsx", index=False)
