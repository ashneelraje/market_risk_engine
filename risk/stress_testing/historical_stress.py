import pandas as pd

def historical_stress_test(pnl: pd.Series, n_worst: int = 10):

    pnl = pnl.dropna()

    worst_losses = pnl.sort_values().head(n_worst)

    stress_df = pd.DataFrame({
        "date": worst_losses.index,
        "pnl": worst_losses.values
    }).reset_index(drop=True)

    stress_df["rank"] = stress_df.index + 1

    return stress_df
