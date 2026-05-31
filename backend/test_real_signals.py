import time
import random

from backend.engine.signal_engine import run_engine
from backend.engine.telegram_builder import send_signal
from backend.engine.tracker import record_trade
from backend.core.config import PAIRS


def start_engine():

    print("🔥 REAL SIGNAL ENGINE RUNNING...")

    while True:

        for pair in PAIRS:

            signal = run_engine(pair)

            if not signal:
                continue

            send_signal(signal)

            print(f"📤 SIGNAL SENT: {pair} {signal['direction']}")

            # ⚠️ SIMULATED RESULT (replace later with broker API)
            result = "WIN" if random.random() > 0.45 else "LOSS"

            record_trade(pair, signal["direction"], result)

            print(f"📊 RESULT: {result}")

        time.sleep(60)