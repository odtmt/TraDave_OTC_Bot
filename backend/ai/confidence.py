import random


def calculate_confidence(score, session):

    base = min(max(score, 0), 100)

    # session boost
    if session == "NEW_YORK":
        base += 10
    elif session == "LONDON":
        base += 7
    else:
        base -= 5

    # noise adjustment
    base += random.randint(-5, 5)

    return max(0, min(100, base))