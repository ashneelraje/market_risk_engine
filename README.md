# Multi-Asset Market Risk Engine

A production-style **market risk engine** for multi-asset portfolios implementing Value-at-Risk (VaR), Expected Shortfall (ES), stress testing, backtesting, and risk attribution.

The system is designed to closely mirror **institutional risk infrastructure** used by banks, asset managers, and systematic trading desks.

---

## Project Objective

To design and implement an end-to-end market risk system that:
- Measures portfolio tail risk across asset classes
- Models correlated asset losses
- Performs regulatory-style VaR backtesting
- Conducts historical and hypothetical stress testing
- Attributes portfolio risk to individual assets using marginal risk principles

---

## Risk Methodologies Implemented

### Value-at-Risk (VaR)
- Historical VaR
- Parametric (Variance–Covariance) VaR
- Monte Carlo VaR

### Expected Shortfall (ES)
- Historical ES
- Monte Carlo ES

---

## Portfolio & PnL Modeling

- Multi-asset portfolio construction
- Log-return–based return modeling
- Dollar P&L–based loss computation
- Correlated return simulation using **Cholesky decomposition**
- Multivariate normal assumptions for parametric and Monte Carlo models

---

## Risk Diagnostics & Validation

- Rolling VaR and Rolling ES computation
- VaR backtesting using **Kupiec Proportion of Failures (POF) test**
- Identification of worst historical losses
- Historical and hypothetical stress testing
- Breach monitoring and exceedance analysis

---

## Risk Attribution

- Marginal VaR
- Component VaR
- Asset-level contribution to portfolio tail risk
- Euler-based decomposition of portfolio VaR

---

## Project Structure

market_risk_engine/     
├── analytics/        
│ └── returns.py       
├── backtesting/      
│ └── var_backtest.py        
├── data/      
│ ├── download_prices.py     
│ ├── raw/
│ │ └── prices.csv         
│ └── processed/    
│ │ ├── historical_stress_losses.csv         
│ │ ├── hypothetical_stress_losses.csv          
│ │ ├── monte_carlo_es.csv           
│ │ ├── rolling_es.csv        
│ │ ├── rolling_var.csv      
│ │ ├── var_backtest_95.csv   
│ │ └── var_backtest_99.csv       
├── risk/       
│ ├── historical_var.py       
│ ├── marginal_var.py    
│ ├── monte_carlo_es.py      
│ ├── monte_carlo_var.py       
│ ├── monte_carlo_simulation.py       
│ ├── parametric_var.py      
│ ├── risk_report.py       
│ ├── rolling_es.py        
│ ├── rolling_var.py      
│ └── stress_testing/      
│ │ ├── historical_stress.py     
│ │ └── hypothetical_stress.py            
├── main.py         
├── visualization.py         
├── README.md         
└── MODEL_ASSUMPTIONS.md

---

## Outputs & Analytics

- Portfolio VaR (95% / 99%)
- Expected Shortfall estimates
- Rolling risk time series
- VaR backtest breach statistics
- Asset-level risk contribution analysis
- Stress scenario loss reports

---

## Tech Stack

- Python
- NumPy
- Pandas
- SciPy
- Quantitative risk modeling & simulation techniques

---

## Intended Use

- Market risk analysis
- Portfolio risk management
- Quantitative research
- Trading desk risk monitoring

---

## Disclaimer

This project is for educational and demonstration purposes only and does not constitute financial or investment advice.
