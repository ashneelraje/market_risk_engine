import pandas as pd
import numpy as np

def hypothetical_stress_test( returns: pd.Series, notional: float, sigmas=(3, 5, 8)):

    vol = returns.std()

    stress_results = []

    for sigma in sigmas:
        shock_return = -sigma * vol
        stress_pnl = shock_return * notional

        stress_results.append({
            "sigma_shock": f"-{sigma}σ",
            "return_shock": shock_return,
            "pnl_loss": stress_pnl
        })

    return pd.DataFrame(stress_results)
