# backend/engine/risk.py

from backend.engine.tracker import get_win_rate


def risk_check():

    win_rate = get_win_rate()

    # adaptive risk control
    if win_rate < 0.35:
        return False

    return True