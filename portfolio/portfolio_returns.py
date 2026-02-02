import pandas as pd
import numpy as np

def compute_portfolio_returns( returns: pd.DataFrame, weights: dict) -> pd.Series:

    if isinstance(returns.columns, pd.MultiIndex):
        returns = returns.copy()
        returns.columns = returns.columns.get_level_values(-1)

    weights_series = pd.Series(weights, dtype=float)
    weights_series = weights_series.reindex(returns.columns)

    if weights_series.isna().any():
        missing = weights_series[weights_series.isna()].index.tolist()
        raise ValueError(f"Missing weights for assets: {missing}")

    portfolio_returns = returns.mul(weights_series, axis=1).sum(axis=1)

    portfolio_returns.name = "Portfolio"
    return portfolio_returns

