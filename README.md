# Multiple Stocks Financial Data Analysis

A Python-based financial data analysis project for downloading, processing, and analyzing historical stock market data. The project focuses on return analysis, descriptive statistics, risk metrics, rolling statistics, drawdowns, and normality testing using Pandas, NumPy, and SciPy.

---

## Features

- Download and clean historical stock price data
- Compute:
  - Daily Log Returns
  - Weekly Returns
  - Monthly Returns
  - Yearly Returns
- Generate descriptive statistics
- Perform risk analysis
- Calculate:
  - Value at Risk (VaR)
  - Expected Shortfall (CVaR)
  - Sharpe Ratio
  - Sortino Ratio
  - Calmar Ratio
  - Maximum Drawdown
  - CAGR
- Rolling 30-Day Analysis
- Normality Testing
  - Jarque-Bera Test
  - Shapiro-Wilk Test
  - D'Agostino K² Test
- Drawdown analysis
- Jupyter Notebook for exploratory data analysis

---

## Project Structure

```
MULTIPLE_STOCKS/
│
├── data/
│   ├── raw/
│   │   └── prices.csv
│   │
│   └── processed/
│       ├── daily_log_returns.csv
│       ├── weekly_returns.csv
│       ├── monthly_returns.csv
│       └── yearly_returns.csv
│
├── notebook/
│   └── 01_data_exploration.ipynb
│
├── plots/
│
├── src/
│   ├── data_loader.py
│   ├── returns.py
│   └── stats.py
│
├── config.py
├── README.md
└── .gitignore
```

---

## Technologies Used

- Python 3.x
- Pandas
- NumPy
- SciPy
- Matplotlib
- Jupyter Notebook

---

## Statistical Metrics

### Descriptive Statistics

- Mean Daily Return
- Annualized Return
- Daily Standard Deviation
- Annualized Volatility
- Skewness
- Excess Kurtosis
- Minimum Return
- Maximum Return
- Naive Sharpe Ratio

---

### Risk Metrics

- Parametric Value at Risk (95%)
- Historical Value at Risk (95%)
- Expected Shortfall (CVaR)
- Sharpe Ratio
- Sortino Ratio
- Semi-Deviation
- Maximum Drawdown
- CAGR
- Calmar Ratio
- Tracking Error *(optional benchmark)*
- Information Ratio *(optional benchmark)*

---

### Normality Tests

The project evaluates whether stock returns follow a normal distribution using:

- Jarque-Bera Test
- Shapiro-Wilk Test
- D'Agostino K² Test

---

### Rolling Analysis

Using a rolling 30-day window:

- Rolling Mean Return
- Rolling Volatility
- Rolling Sharpe Ratio

---

### Drawdown Analysis

For each stock:

- Running Maximum Price
- Drawdown Series
- Maximum Drawdown

---

## Workflow

```
Historical Prices
        │
        ▼
Data Cleaning
        │
        ▼
Return Calculation
        │
        ▼
Descriptive Statistics
        │
        ▼
Risk Analysis
        │
        ▼
Rolling Metrics
        │
        ▼
Normality Testing
        │
        ▼
Visualization
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/multiple-stocks-analysis.git

cd multiple-stocks-analysis
```

Install dependencies

```bash
pip install pandas numpy scipy matplotlib jupyter yfinance
```

---

## Usage

Run the Jupyter notebook:

```bash
jupyter notebook notebook/01_data_exploration.ipynb
```

Or import the modules directly:

```python
from src.stats import descriptive
from src.stats import risk_analysis
from src.stats import normality
from src.stats import rolling_metrics
from src.stats import drawdown_series
```

---

## Example Outputs

The project generates:

- Processed return datasets
- Summary statistics tables
- Risk metrics tables
- Rolling performance metrics
- Drawdown analysis
- Distribution and return visualizations

---

## Future Improvements

- CAPM Metrics
- Beta & Alpha
- Portfolio Optimization
- Efficient Frontier
- Monte Carlo Portfolio Simulation
- Fama-French Factor Models
- GARCH Volatility Forecasting
- Correlation Heatmaps
- Interactive Plotly Dashboard
- Automated Report Generation

---

## Learning Objectives

This project demonstrates practical applications of:

- Financial Time Series Analysis
- Risk Management
- Quantitative Finance
- Statistical Analysis
- Portfolio Performance Evaluation
- Python for Financial Data Science

---

## License

This project is intended for educational and research purposes.