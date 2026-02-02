import pandas as pd
import numpy as np

def rolling_expected_shortfall(pnl, window=252, confidence=0.95):

    def es(x):
        var_threshold = np.quantile(x, 1 - confidence)
        return x[x <= var_threshold].mean()

    return pnl.rolling(window).apply(es, raw=False)
