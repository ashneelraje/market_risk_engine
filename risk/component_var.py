import pandas as pd
import numpy as np


def historical_component_var( asset_returns: pd.DataFrame, weights: dict, notional: float, confidence: float = 0.95) -> pd.DataFrame:

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

    asset_pnl = asset_returns.loc[var_date] * weights_series * notional

    component_var = -asset_pnl

    portfolio_var = -var_threshold
    component_var = component_var * (portfolio_var / component_var.sum())

    result = pd.DataFrame({
        "Component_VaR": component_var,
        "Component_%": component_var / portfolio_var
    })

    return result
