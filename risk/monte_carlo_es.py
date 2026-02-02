import numpy as np

def monte_carlo_expected_shortfall(
    pnl: np.ndarray,
    confidence: float = 0.95
) -> float:

    var_threshold = np.percentile(pnl, (1 - confidence) * 100)
    es = -pnl[pnl <= var_threshold].mean()
    return es
