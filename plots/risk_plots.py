import matplotlib.pyplot as plt
import pandas as pd

def plot_var_vs_es():
    var = pd.read_csv("data/processed/rolling_var.csv", index_col=0, parse_dates=True)
    es = pd.read_csv("data/processed/rolling_es.csv", index_col=0, parse_dates=True)

    plt.figure(figsize=(12, 6))

    plt.plot(var.index, var["VaR_95"], label="VaR 95%", linestyle="--")
    plt.plot(es.index, es["ES_95"], label="ES 95%", linewidth=2)

    plt.plot(var.index, var["VaR_99"], label="VaR 99%", linestyle="--")
    plt.plot(es.index, es["ES_99"], label="ES 99%", linewidth=2)

    plt.title("Rolling VaR vs Expected Shortfall")
    plt.ylabel("Dollar Loss")
    plt.legend()
    plt.grid(True)

    plt.show()
