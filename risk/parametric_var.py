import numpy as np
import pandas as pd
from scipy.stats import norm


def parametric_var(
    returns: pd.DataFrame,
    weights: dict,
    notional: float,
    confidence: float = 0.95
) -> float:

    w = pd.Series(weights).reindex(returns.columns).values

    cov_matrix = returns.cov().values

    portfolio_vol = np.sqrt(w.T @ cov_matrix @ w)

    z_score = norm.ppf(confidence)

    var = z_score * portfolio_vol * notional

    return var



def parametric_component_var(
    returns: pd.DataFrame,
    weights: dict,
    notional: float,
    confidence: float = 0.95
) -> pd.DataFrame:

    w = pd.Series(weights).reindex(returns.columns)
    cov = returns.cov()

    z = norm.ppf(confidence)
    port_vol = np.sqrt(w.T @ cov @ w)

    marginal_var = z * (cov @ w) / port_vol * notional
    component_var = w * marginal_var

    df = pd.DataFrame({
        "Component_VaR": component_var,
        "Component_%": component_var / component_var.sum(),
        "Marginal_VaR": marginal_var
    })
    return df