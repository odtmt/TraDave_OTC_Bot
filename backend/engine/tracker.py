# backend/engine/tracker.py

trade_history = []


def record_trade(pair, direction, result):

    trade_history.append({
        "pair": pair,
        "direction": direction,
        "result": result
    })


def get_win_rate():

    if not trade_history:
        return 0.5

    wins = len([t for t in trade_history if t["result"] == "WIN"])

    return wins / len(trade_history)