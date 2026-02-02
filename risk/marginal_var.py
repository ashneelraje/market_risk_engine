import pandas as pd
import numpy as np


def historical_marginal_var( asset_returns: pd.DataFrame, weights: dict, notional: float, confidence: float = 0.95) -> pd.Series:

    if isinstance(asset_returns.columns, pd.MultiIndex):
        asset_returns = asset_returns.copy()
        asset_returns.columns = asset_returns.columns.get_level_values(-1)

    weights_series = pd.Series(weights).reindex(asset_returns.columns)

    portfolio_returns = asset_returns.mul(weights_series, axis=1).sum(axis=1)
    portfolio_pnl = portfolio_returns * notional

    var_threshold = np.percentile(
        portfolio_pnl,
        (1 - confidence) * 100
    )

    var_date = portfolio_pnl[portfolio_pnl <= var_threshold].idxmax()

    marginal_var = -asset_returns.loc[var_date] * notional
    marginal_var.name = "Marginal_VaR"

    return marginal_var
