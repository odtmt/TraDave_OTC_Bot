from config import MIN_CONFIDENCE
import numpy as np

def get_signal(prob, row):

    # safety check (prevents NaN crashes)
    if row.isnull().any():
        return "NO_TRADE"

    score = 0

    # trend direction
    if row["ma_fast"] > row["ma_slow"]:
        score += 1
    else:
        score -= 1

    # RSI filter (more stable logic)
    if row["rsi"] < 30:
        score += 1
    elif row["rsi"] > 70:
        score -= 1

    # AI probability safety check
    prob = np.array(prob)

    # FIX: ensure correct indexing safety
    if len(prob) < 2:
        return "NO_TRADE"

    bullish_prob = float(prob[1])
    bearish_prob = float(prob[0])

    # confidence logic (smoothed)
    if bullish_prob > MIN_CONFIDENCE:
        score += 2
    elif bearish_prob > MIN_CONFIDENCE:
        score -= 2

    # FINAL DECISION (with buffer zone improvement)
    if score >= 3:
        return "CALL"
    elif score <= -3:
        return "PUT"

    return "NO_TRADE"