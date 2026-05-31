from backend.telegram_sender import send_telegram_message
from datetime import datetime
from zoneinfo import ZoneInfo


def get_nigeria_time():
    return datetime.now(ZoneInfo("Africa/Lagos")).strftime("%H:%M:%S WAT")


def main():

    print("🔥 Testing Telegram connection (Nigeria Time)...")

    entry_time = get_nigeria_time()

    message = f"""
🔔 TEST SIGNAL

🕒 ENTRY TIME: {entry_time} (Nigeria Time)

📊 Pair: EURUSD
📈 Direction: BUY
⏳ Timeframe: 3M

🚀 Status: TELEGRAM TEST SUCCESS
""".strip()

    result = send_telegram_message(message)

    print("RESULT:", result)

    if result and result.get("ok"):
        print("✅ Telegram SUCCESS")
    else:
        print("❌ Telegram FAILED")


if __name__ == "__main__":
    main()