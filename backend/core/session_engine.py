from datetime import datetime
from zoneinfo import ZoneInfo


def get_nigeria_hour():

    now = datetime.now(ZoneInfo("Africa/Lagos"))
    return now.hour


def get_trading_session():

    hour = get_nigeria_hour()

    # 🇬🇧 London Session (8AM - 4PM WAT)
    if 8 <= hour < 16:
        return "LONDON", 1.5  # boost multiplier

    # 🇺🇸 New York Session (1PM - 10PM WAT)
    if 13 <= hour < 22:
        return "NEW_YORK", 1.7  # strongest session

    # 🌙 OTC / Low liquidity
    return "OTC", 0.8