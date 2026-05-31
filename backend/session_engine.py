from datetime import datetime

def get_session():

    hour = datetime.utcnow().hour

    if 6 <= hour < 13:
        return "LONDON"
    elif 13 <= hour < 20:
        return "NEW_YORK"
    elif 0 <= hour < 6:
        return "ASIA"
    else:
        return "OFF"


def is_good_session(session):
    return session in ["LONDON", "NEW_YORK"]