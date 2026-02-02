import numpy as np
import pandas as pd

def historical_var( pnl: pd.Series, confidence: float = 0.95) -> float:
   
    if not 0 < confidence < 1:
        raise ValueError("Confidence level must be between 0 and 1")

    var = -np.percentile(pnl, (1 - confidence) * 100)
    return var
