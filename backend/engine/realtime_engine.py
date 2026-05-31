import time
import random

from backend.engine.signal_engine import run_engine
from backend.engine.telegram_builder import send_signal
from backend.engine.tracker import record_trade
from backend.core.config import PAIRS


def start_engine():

    print("🔥 ENGINE STARTED — DEBUG MODE ACTIVE")

    while True:

        for pair in PAIRS:

            print(f"🔍 SCANNING: {pair}")  # ✅ MUST SEE THIS

            signal = run_engine(pair)

            print("SIGNAL RESULT:", signal)  # ✅ CRITICAL DEBUG

            if not signal:
                continue

            send_signal(signal)

            print(f"📤 SENT: {pair} {signal['direction']}")

            result = "WIN" if random.random() > 0.45 else "LOSS"

            record_trade(pair, signal["direction"], result)

            print(f"📊 RESULT: {result}")

        time.sleep(5)