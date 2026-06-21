import pandas as pd
import numpy as np
import scipy.stats as stats


def descriptive(returns):
    out = pd.DataFrame(index=returns.columns)

    out["mean_daily"] = returns.mean()
    out["mean_annual"] = returns.mean() * 252

    out["std_daily"] = returns.std()
    out["vol_annual"] = returns.std() * np.sqrt(252)

    out["skewness"] = returns.skew()
    out["excess_kurtosis"] = returns.kurtosis()

    out["min"] = returns.min()
    out["max"] = returns.max()

    out["sharpe_naive"] = out["mean_annual"] / out["vol_annual"]

    return out.round(4)


def risk_analysis(returns, benchmark_returns=None, risk_free_rate=0.05):
    out = pd.DataFrame(index=returns.columns)

    out["Parametric VaR"] = returns.mean() - 1.645 * returns.std()
    out["Historical VaR"] = returns.quantile(0.05)
    out["Expected Shortfall"] = returns.apply(lambda x: x[x <= x.quantile(0.05)].mean())

    annual_return = returns.mean() * 252
    annual_volatility = returns.std() * np.sqrt(252)

    out["Sharpe Ratio"] = (annual_return - risk_free_rate) / annual_volatility

    downside_volatility = returns.apply(lambda x: x[x < 0].std())

    out["Semi Deviation"] = downside_volatility

    out["Sortino Ratio"] = (annual_return - risk_free_rate) / (
        downside_volatility * np.sqrt(252)
    )

    wealth_index = (1 + returns).cumprod()
    running_peak = wealth_index.cummax()
    drawdown = (wealth_index - running_peak) / running_peak

    max_drawdown = drawdown.min()

    out["Max Drawdown"] = max_drawdown

    years = len(returns) / 252
    cagr = wealth_index.iloc[-1] ** (1 / years) - 1

    out["CAGR"] = cagr
    out["Calmar Ratio"] = cagr / abs(max_drawdown)

    if benchmark_returns is not None:
        active_returns = returns.subtract(benchmark_returns.squeeze(), axis=0)

        annual_benchmark_return = benchmark_returns.mean() * 252
        active_return = annual_return - annual_benchmark_return
        tracking_error = active_returns.std() * np.sqrt(252)

        out["Tracking Error"] = tracking_error
        out["Information Ratio"] = active_return / tracking_error

    return out.round(4)

def normality(returns):
    results = []

    for col in returns.columns:
        x = returns[col].dropna()
        jb_stat, jb_p = stats.jarque_bera(x)
        if len(x) <= 5000:
            sw_stat, sw_p = stats.shapiro(x)
        else:
            sw_stat, sw_p = np.nan, np.nan
        if len(x) >= 8:
            da_stat, da_p = stats.normaltest(x)
        else:
            da_stat, da_p = np.nan, np.nan

        results.append({
            "Stock": col,
            "Jarque-Bera Stat": round(jb_stat, 3),
            "Jarque-Bera p": round(jb_p, 5),
            "JB Reject": jb_p < 0.05,

            "Shapiro Stat": round(sw_stat, 3) if not np.isnan(sw_stat) else None,
            "Shapiro p": round(sw_p, 5) if not np.isnan(sw_p) else None,
            "SW Reject": sw_p < 0.05 if not np.isnan(sw_p) else None,

            "D'Agostino Stat": round(da_stat, 3) if not np.isnan(da_stat) else None,
            "D'Agostino p": round(da_p, 5) if not np.isnan(da_p) else None,
            "DA Reject": da_p < 0.05 if not np.isnan(da_p) else None,
        })
    return pd.DataFrame(results)