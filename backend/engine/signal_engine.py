from backend.engine.strategy import detect_signal
from backend.engine.risk import risk_check
from backend.engine.execution_guard import can_execute
from datetime import datetime


def run_engine(pair):

    signal = detect_signal(pair)

    if not signal:
        return None

    if not risk_check():
        return None

    if not can_execute(pair):
        return None

    # 🔥 GLIVABOT STYLE ENTRY TIME (IMPORTANT FIX)
    signal["entry_time"] = datetime.utcnow().strftime("%H:%M UTC")

    return signal