import random


def get_candles(pair, timeframe="3M", limit=50):

    # ⚠️ TEMP: simulated OHLC data
    # Replace later with Deriv / MT5 / Binance API

    candles = []

    price = random.uniform(1.0500, 1.0600)

    for _ in range(limit):

        open_p = price
        close_p = price + random.uniform(-0.002, 0.002)
        high = max(open_p, close_p) + random.uniform(0, 0.001)
        low = min(open_p, close_p) - random.uniform(0, 0.001)

        candles.append({
            "open": open_p,
            "high": high,
            "low": low,
            "close": close_p
        })

        price = close_p

    return candles