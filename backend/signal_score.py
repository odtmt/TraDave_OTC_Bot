def score_signal(confidence, session, volatility_ok=True):

    base_score = confidence

    # 🌍 session weighting
    session_boost = {
        "LONDON": 5,
        "NEW_YORK": 7,
        "ASIA": 3
    }

    score = base_score + session_boost.get(session, 0)

    # 📉 penalize bad market conditions
    if not volatility_ok:
        score -= 15

    # clamp range
    return max(0, min(100, score))