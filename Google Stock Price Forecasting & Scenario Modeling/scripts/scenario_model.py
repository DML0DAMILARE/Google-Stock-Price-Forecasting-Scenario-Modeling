# scenario_model.py

from load import df
from forecast_model import forecast
import pandas as pd

# --- Safely compute volatility mean ---
try:
    volatility_mean = pd.to_numeric(df['volatility'], errors='coerce').mean()
except Exception:
    volatility_mean = 0  # fallback in case 'volatility' is missing or invalid

# --- Scenario modeling ---
forecast['best_case'] = forecast['yhat'] * 1.1
forecast['worst_case'] = forecast['yhat'] * 0.9 - (volatility_mean * 50)

# --- Export scenarios ---
forecast[['ds', 'best_case']].to_excel("outputs/scenario_best_case.xlsx", index=False)
forecast[['ds', 'worst_case']].to_excel("outputs/scenario_worst_case.xlsx", index=False)
