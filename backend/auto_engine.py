import time

from backend.signal_engine import run_engine
from backend.signal_formatter import format_signal
from backend.notifications.push import send_push

DEVICE_TOKEN = "YOUR_DEVICE_TOKEN_HERE"

INTERVAL = 60


def start_bot():

    print("🔥 OTC AUTO SIGNAL ENGINE STARTED")

    while True:

        try:
            data = run_engine("EURUSD=X")

            if data:

                formatted = format_signal(
                    data["pair"],
                    data["signal"],
                    data["confidence"]
                )

                send_push(
                    formatted["title"],
                    formatted["body"],
                    DEVICE_TOKEN
                )

                print("✅ Signal sent:", data)

            else:
                print("⚪ No signal this cycle")

        except Exception as e:
            print("❌ Error:", e)

        time.sleep(INTERVAL)


if __name__ == "__main__":
    start_bot()