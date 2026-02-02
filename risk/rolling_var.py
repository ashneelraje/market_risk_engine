import numpy as np
import pandas as pd

def rolling_historical_var(
    pnl: pd.Series,
    window: int = 252,
    confidence: float = 0.95
) -> pd.Series:

    def var_func(x):
        return -np.percentile(x, (1 - confidence) * 100)

    rolling_var = pnl.rolling(window).apply(var_func, raw=True)
    return rolling_var
