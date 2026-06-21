import numpy as np

def log_ret(prices):
    return np.log(prices / prices.shift(1)).dropna()