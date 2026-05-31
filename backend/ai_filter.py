def filter_signal(signal, confidence):

    # reject weak signals
    if confidence < 70:
        return False

    # optional rule-based filter
    if signal not in ["BUY", "SELL"]:
        return False

    return True