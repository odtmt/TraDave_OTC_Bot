from backend.session_engine import get_session


def get_pairs():

    session = get_session()

    if session == "LONDON":
        return ["EURUSD", "GBPUSD", "EURGBP", "USDCHF"]

    elif session == "NEW_YORK":
        return ["EURUSD", "USDJPY", "GBPUSD", "USDCAD"]

    else:
        return ["USDJPY", "AUDUSD", "NZDUSD", "AUDJPY"]