import pandas as pd

from analytics.returns import compute_log_returns

from backtesting.var_backtest import var_backtest

from data.download_prices import download_prices

from portfolio.portfolio_returns import compute_portfolio_returns

from risk.component_var import historical_component_var
from risk.marginal_var import historical_marginal_var
from risk.expected_shortfall import historical_expected_shortfall
from risk.historical_var import historical_var
from risk.parametric_var import parametric_var, parametric_component_var
from risk.monte_carlo_simulation import simulate_portfolio_pnl
from risk.monte_carlo_var import monte_carlo_var
from risk.monte_carlo_es import monte_carlo_expected_shortfall
from risk.risk_report import generate_risk_report
from risk.rolling_es import rolling_expected_shortfall
from risk.rolling_var import rolling_historical_var
from risk.stress_testing.historical_stress import historical_stress_test
from risk.stress_testing.hypothetical_stress import hypothetical_stress_test


START_DATE = "2010-01-01"
END_DATE = "2024-01-01"
TICKERS = ["SPY", "TLT", "GLD"]
WEIGHTS = {"SPY": 0.60, "TLT": 0.25, "GLD": 0.15}
NOTIONAL = 1000000  


def main():

    prices = download_prices(TICKERS, START_DATE, END_DATE)
    prices.to_csv("data/raw/prices.csv")

    asset_returns = compute_log_returns(prices)
    if isinstance(asset_returns.columns, pd.MultiIndex):
        asset_returns.columns = asset_returns.columns.get_level_values(1)
    asset_returns.to_csv("outputs/log_returns.csv")

    portfolio_returns = compute_portfolio_returns(asset_returns, WEIGHTS)
    portfolio_returns.name = "Portfolio"
    portfolio_returns.to_csv("outputs/portfolio_returns.csv")

    pnl = NOTIONAL * portfolio_returns
    pnl.name = "PnL"
    pnl.to_csv("outputs/pnl.csv")

    var_95 = historical_var(pnl, confidence=0.95)
    var_99 = historical_var(pnl, confidence=0.99)
    print(f"Historical VaR (95%): ${var_95:,.2f}")
    print(f"Historical VaR (99%): ${var_99:,.2f}")

    param_var_95 = parametric_var( returns=asset_returns, weights=WEIGHTS, notional=NOTIONAL, confidence=0.95)
    param_var_99 = parametric_var( returns=asset_returns, weights=WEIGHTS, notional=NOTIONAL, confidence=0.99)
    print(f"Parametric VaR (95%): ${param_var_95:,.2f}")
    print(f"Parametric VaR (99%): ${param_var_99:,.2f}")

    parametric_decomp = parametric_component_var( returns=asset_returns, weights=WEIGHTS, notional=NOTIONAL, confidence=0.95)
    parametric_decomp.to_csv( "outputs/parametric_var_decomposition.csv")

    simulated_pnl = simulate_portfolio_pnl( returns=asset_returns, weights=WEIGHTS, notional=NOTIONAL, n_simulations=100_000)
    mc_var_95 = monte_carlo_var(simulated_pnl, confidence=0.95)
    mc_var_99 = monte_carlo_var(simulated_pnl, confidence=0.99)
    print(f"Monte Carlo VaR (95%): ${mc_var_95:,.2f}")
    print(f"Monte Carlo VaR (99%): ${mc_var_99:,.2f}")

    mc_es_95 = monte_carlo_expected_shortfall(simulated_pnl, confidence=0.95)
    mc_es_99 = monte_carlo_expected_shortfall(simulated_pnl, confidence=0.99)
    mc_es_df = pd.DataFrame({ "confidence": [0.95, 0.99], "MonteCarlo_ES": [mc_es_95, mc_es_99]})
    mc_es_df.to_csv("data/processed/monte_carlo_es.csv", index=False)

    rolling_var_95 = rolling_historical_var(pnl, window=252, confidence=0.95)
    rolling_var_99 = rolling_historical_var(pnl, window=252, confidence=0.99)
    rolling_var_df = pd.DataFrame({ "VaR_95": rolling_var_95, "VaR_99": rolling_var_99 })
    rolling_var_df.to_csv("data/processed/rolling_var.csv")

    profit_n_loss = pd.read_csv( "outputs/pnl.csv", index_col=0, parse_dates=True )["PnL"]
    var_df = pd.read_csv( "data/processed/rolling_var.csv", index_col=0, parse_dates=True)

    bt_95, stats_95 = var_backtest( profit_n_loss, var_df["VaR_95"], alpha=0.95)
    bt_95.to_csv("data/processed/var_backtest_95.csv")

    bt_99, stats_99 = var_backtest( profit_n_loss, var_df["VaR_99"], alpha=0.99)
    bt_99.to_csv("data/processed/var_backtest_99.csv")

    print("VaR 95% Backtest Stats:", stats_95)
    print("VaR 99% Backtest Stats:", stats_99)

    pnl = pd.read_csv( "outputs/pnl.csv", index_col=0, parse_dates=True)["PnL"]

    stress_df = historical_stress_test(pnl, n_worst=10)
    stress_df.to_csv("data/processed/historical_stress_losses.csv", index=False)

    print("\nWorst Historical Losses:")
    print(stress_df)

    returns = pd.read_csv( "outputs/portfolio_returns.csv", index_col=0, parse_dates=True)["Portfolio"]
    stress_hypo_df = hypothetical_stress_test( returns=returns, notional=NOTIONAL, sigmas=(3, 5, 8))
    stress_hypo_df.to_csv( "data/processed/hypothetical_stress_losses.csv", index=False)

    es_95 = historical_expected_shortfall(pnl, confidence=0.95)
    es_99 = historical_expected_shortfall(pnl, confidence=0.99)
    print(f"Expected Shortfall (95%): ${es_95:,.2f}")
    print(f"Expected Shortfall (99%): ${es_99:,.2f}")

    rolling_es_95 = rolling_expected_shortfall(pnl, window=252, confidence=0.95)
    rolling_es_99 = rolling_expected_shortfall(pnl, window=252, confidence=0.99)
    rolling_es_df = pd.DataFrame({ "ES_95": rolling_es_95, "ES_99": rolling_es_99})
    rolling_es_df.to_csv("data/processed/rolling_es.csv")

    worst_losses = pd.read_csv("data/processed/historical_stress_losses.csv")

    component_var_df = historical_component_var( asset_returns=asset_returns, weights=WEIGHTS, notional=NOTIONAL, confidence=0.95)
    component_var_df.to_csv("outputs/historical_component_var.csv")

    marginal_var = historical_marginal_var( asset_returns=asset_returns, weights=WEIGHTS, notional=NOTIONAL, confidence=0.95)
    marginal_var.to_csv("outputs/historical_marginal_var.csv")

    risk_report = generate_risk_report( var_95, var_99, rolling_es_95.dropna().iloc[-1], rolling_es_99.dropna().iloc[-1], worst_losses)
    risk_report.to_csv("outputs/risk_summary_report.csv")

if __name__ == "__main__":
    main()
