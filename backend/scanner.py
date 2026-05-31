import time

from backend.pair_selector import get_pairs
from backend.signal_engine import run_engine
from backend.signal_formatter import format_signal
from backend.telegram_sender import send_telegram_message
from backend.trade_journal import log_trade


BOT_TOKEN = "8616204763:AAFGou1ne2g5b6UuvtPasmi56VTyHzlORM8>/getUpdates"
CHAT_ID = "7183440669"

MIN_SCORE = 75
COOLDOWN = 120

last_sent = {}


def can_send(pair):
    now = time.time()
    return now - last_sent.get(pair, 0) > COOLDOWN


def mark_sent(pair):
    last_sent[pair] = time.time()


def scan_market():

    for pair in get_pairs():

        if not can_send(pair):
            continue

        data = run_engine(pair)

        if not data:
            continue

        # 🧠 FINAL FILTER (SMART ENGINE)
        if data["score"] < MIN_SCORE:
            print(f"⚪ SKIP {pair} | score={data['score']}")
            continue

        formatted = format_signal(
            data["pair"],
            data["signal"],
            data["confidence"],
            data["entry_time"]
        )

        res = send_telegram_message(formatted["body"])

        if res.get("ok"):

            mark_sent(pair)

            # 🧾 log trade
            log_trade(data)

            print(
                f"📤 SENT {pair} | "
                f"{data['signal']} | "
                f"conf={data['confidence']} | "
                f"score={data['score']} | "
                f"time={data['entry_time']}"
            )

        else:
            print(f"❌ FAILED {pair}")