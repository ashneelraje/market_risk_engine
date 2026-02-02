import numpy as np

def monte_carlo_var(
    pnl: np.ndarray,
    confidence: float = 0.95
) -> float:

    var = -np.percentile(pnl, (1 - confidence) * 100)
    return var
