import numpy as np

def log_ret(prices):
    return np.log(prices / prices.shift(1)).dropna()

def week_ret(prices):
    week = prices.resample("W").last()
    return week.pct_change().dropna()

def month_ret(prices):
    month = prices.resample("ME").last()
    return month.pct_change().dropna()

def year_ret(prices):
    year = prices.resample("YE").last()
    return year.pct_change().dropna()