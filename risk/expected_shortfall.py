import numpy as np
import pandas as pd

def historical_expected_shortfall(pnl: pd.Series, confidence: float = 0.99):
   
    losses = -pnl  # convert to losses
    var_threshold = np.quantile(losses, confidence)

    tail_losses = losses[losses >= var_threshold]

    return tail_losses.mean()
