from backend.engine.indicators import get_indicators
from backend.core.session_engine import get_trading_session
import random


def detect_signal(pair):

    ind = get_indicators(pair)

    session, multiplier = get_trading_session()

    score = 50  # neutral base

    # ---------------- RSI ----------------
    if ind["rsi"] < 30:
        score += 20
    elif ind["rsi"] > 70:
        score -= 20
    else:
        score += 5

    # ---------------- EMA ----------------
    if ind["ema_fast"] > ind["ema_slow"]:
        score += 20
    else:
        score -= 20

    # ---------------- VOLATILITY ----------------
    if 0.8 <= ind["volatility"] <= 1.5:
        score += 10
    else:
        score -= 10

    # ---------------- SESSION BOOST ----------------
    score = score * multiplier

    # ---------------- MARKET NOISE SIMULATION ----------------
    if random.random() > 0.90:
        score += random.randint(-10, 10)

    # ---------------- SESSION RULES ----------------

    # 🔥 High quality signals in NY/London only
    if session in ["LONDON", "NEW_YORK"]:

        if score >= 70:
            return {
                "pair": pair,
                "direction": "BUY",
                "score": round(score, 2),
                "session": session,
                "timeframe": "3M"
            }

        if score <= 30:
            return {
                "pair": pair,
                "direction": "SELL",
                "score": round(score, 2),
                "session": session,
                "timeframe": "3M"
            }

    # 🌙 OTC MODE (weaker signals allowed but reduced strength)
    else:

        if score >= 80:
            return {
                "pair": pair,
                "direction": "BUY",
                "score": round(score, 2),
                "session": session,
                "timeframe": "3M"
            }

        if score <= 20:
            return {
                "pair": pair,
                "direction": "SELL",
                "score": round(score, 2),
                "session": session,
                "timeframe": "3M"
            }

    return None