import numpy as np
import pandas as pd
from scipy.stats import chi2

def var_backtest(returns, var_series, alpha):

    df = pd.DataFrame({
        "return": returns,
        "VaR": var_series
    }).dropna()

    df["breach"] = (df["return"] < -df["VaR"]).astype(int)

    T = len(df)
    failures = df["breach"].sum()
    expected_failures = T * (1 - alpha)

    # Kupiec POF Test
    p_hat = failures / T if failures > 0 else 1e-6
    p = 1 - alpha

    LR_pof = -2 * (
        (T - failures) * np.log((1 - p) / (1 - p_hat)) +
        failures * np.log(p / p_hat)
    )

    p_value = 1 - chi2.cdf(LR_pof, df=1)

    stats = {
        "observations": T,
        "expected_breaches": expected_failures,
        "actual_breaches": failures,
        "breach_ratio": failures / expected_failures if expected_failures > 0 else np.nan,
        "LR_pof": LR_pof,
        "p_value": p_value
    }

    return df, stats
