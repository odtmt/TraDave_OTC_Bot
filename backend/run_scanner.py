import time
import sys
import os

# 🔥 Ensure backend is always importable no matter where you run from
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)
sys.path.append(PROJECT_ROOT)

from backend.scanner import scan_market


INTERVAL = 60  # seconds


def main():

    print("🔥 OTC BOT RUNNING...")

    while True:

        try:
            scan_market()

        except Exception as e:
            print("❌ Scanner crash:", e)

        print("⏳ Waiting for next scan...\n")

        time.sleep(INTERVAL)


if __name__ == "__main__":
    main()