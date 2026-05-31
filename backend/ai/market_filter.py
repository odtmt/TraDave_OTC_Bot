def is_good_market(df):

    volatility = df["close"].std()
    trend = abs(df["ma_fast"].iloc[-1] - df["ma_slow"].iloc[-1])

    if volatility < 0.0005:
        return False

    if volatility > 0.01:
        return False

    if trend < 0.0002:
        return False

    return True