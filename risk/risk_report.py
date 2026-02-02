import pandas as pd

def generate_risk_report(var_95, var_99, es_95, es_99, worst_losses):
    report = {
        "VaR_95": var_95,
        "VaR_99": var_99,
        "ES_95": es_95,
        "ES_99": es_99,
        "Worst_Loss": worst_losses.iloc[0]["pnl"],
        "Worst_Loss_Date": worst_losses.iloc[0]["date"]
    }

    return pd.DataFrame.from_dict(report, orient="index", columns=["Value"])
