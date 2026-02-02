# Model Assumptions — Multi-Asset Market Risk Engine

This document outlines the key modeling assumptions underlying the risk methodologies implemented in the Market Risk Engine.

---

## 1. Return Modeling Assumptions

- Asset returns are modeled using **log returns**
- Returns are assumed to be **stationary** over the estimation window
- Historical return distributions are representative of future risk
- Missing data is handled through aligned time-series preprocessing

---

## 2. Distributional Assumptions

### Parametric VaR
- Asset returns follow a **multivariate normal distribution**
- Mean and covariance are estimated using historical returns
- Linear portfolio aggregation is assumed

### Monte Carlo Simulation
- Simulated returns are drawn from a multivariate normal distribution
- Cross-asset dependencies are captured using the **Cholesky decomposition**
- Tail risk is inferred from simulated PnL distributions

---

## 3. Correlation & Dependency Structure

- Asset correlations are assumed to be stable within the estimation window
- Correlation matrix is positive semi-definite
- No regime-switching or time-varying correlation modeling is applied

---

## 4. PnL and Portfolio Assumptions

- Portfolio positions are assumed to be static during each risk horizon
- PnL is computed in dollar terms using portfolio weights and returns
- No intraday rebalancing is assumed
- No liquidity constraints are explicitly modeled

---

## 5. Backtesting Assumptions

- VaR backtesting uses a **binary exceedance framework**
- Kupiec Proportion of Failures (POF) test assumes independent violations
- Backtests are evaluated at fixed confidence levels (95%, 99%)

---

## 6. Stress Testing Assumptions

### Historical Stress Testing
- Historical crisis periods are representative of extreme market behavior
- Losses are computed using realized historical return shocks

### Hypothetical Stress Testing
- Stress scenarios are user-defined and deterministic
- Shock magnitudes are applied uniformly across relevant assets
- Second-order effects are not modeled

---

## 7. Risk Attribution Assumptions

- Portfolio risk is assumed to be **Euler-decomposable**
- Marginal VaR is computed using local sensitivity approximations
- Component VaR sums to total portfolio VaR

---

## 8. Model Limitations

- Normality assumptions may underestimate extreme tail risk
- Correlations may break down during crisis periods
- No stochastic volatility or fat-tailed distributions are modeled
- Results are sensitive to the chosen estimation window

---

## 9. Intended Scope

This risk engine is intended for:
- Educational use
- Quantitative research
- Conceptual demonstration of institutional risk systems

It is **not** intended for live trading or regulatory capital calculation.
