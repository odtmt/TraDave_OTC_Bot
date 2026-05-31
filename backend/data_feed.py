import random

def get_candles(symbol):

    # mock candles (replace later with real broker/data API)
    return {
        "Close": [1.10 + random.uniform(-0.01, 0.01) for _ in range(50)]
    }