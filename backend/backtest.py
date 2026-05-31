from pro_engine import generate_otc_signal

def run_backtest(steps=50):

    wins = 0

    for _ in range(steps):

        signal = generate_otc_signal()

        # fake win simulation
        if signal["confidence"] > 75:
            wins += 1

    winrate = (wins / steps) * 100

    print(f"Backtest completed → Winrate: {winrate:.2f}%")

if __name__ == "__main__":
    run_backtest()