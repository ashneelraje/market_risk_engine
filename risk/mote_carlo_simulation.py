import numpy as np
import pandas as pd

def simulate_portfolio_pnl(
    returns: pd.DataFrame,
    weights: dict,
    notional: float,
    n_simulations: int = 100_000
) -> np.ndarray:

    w = pd.Series(weights).reindex(returns.columns).values

    mu = returns.mean().values
    cov = returns.cov().values

    L = np.linalg.cholesky(cov)

    Z = np.random.randn(n_simulations, len(w))
    simulated_returns = mu + Z @ L.T

    portfolio_returns = simulated_returns @ w
    pnl = notional * portfolio_returns

    return pnl
