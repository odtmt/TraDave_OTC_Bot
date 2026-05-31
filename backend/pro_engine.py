import random
from pair_selector import get_active_pairs

def generate_otc_signal():

    pairs = get_active_pairs()

    pair = random.choice(pairs)

    signal = random.choice(["BUY", "SELL"])

    confidence = random.randint(65, 95)

    price = round(random.uniform(1.05000, 1.25000), 5)

    return {
        "pair": pair,
        "signal": signal,
        "confidence": confidence,
        "price": price
    }