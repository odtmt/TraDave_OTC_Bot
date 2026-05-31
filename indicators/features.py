import ta

def compute_features(df):

    df["rsi"] = ta.momentum.RSIIndicator(df["close"]).rsi()
    df["ma_fast"] = df["close"].rolling(5).mean()
    df["ma_slow"] = df["close"].rolling(20).mean()
    df["returns"] = df["close"].pct_change()

    df.dropna(inplace=True)
    return df