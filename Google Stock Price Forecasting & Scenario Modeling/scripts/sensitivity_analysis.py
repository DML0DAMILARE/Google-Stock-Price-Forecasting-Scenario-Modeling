import pandas as pd
from forecast_model import forecast

def test_sensitivity(base, change_rates):
    return {f"{int(r*100)}% change": base * (1 + r) for r in change_rates}

sens = test_sensitivity(forecast['yhat'], [-0.1, -0.05, 0, 0.05, 0.1])
pd.DataFrame(sens).to_excel("outputs/sensitivity_analysis.xlsx")
