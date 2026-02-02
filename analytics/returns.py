import numpy as np
import pandas as pd

def compute_log_returns(prices: pd.Series) -> pd.Series:
   
    returns = np.log(prices / prices.shift(1))
    returns = returns.dropna()
    return returns
