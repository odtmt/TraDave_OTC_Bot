# backend/engine/indicators.py

import random


def get_indicators(pair):

    # Replace later with real broker OHLC data
    return {
        "rsi": random.randint(10, 90),
        "ema_fast": random.uniform(1.0500, 1.0600),
        "ema_slow": random.uniform(1.0450, 1.0550),
        "volatility": random.uniform(0.3, 2.0)
    }