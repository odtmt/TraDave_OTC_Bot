# backend/core/config.py

BOT_NAME = "AI_OTC_TRADING_BOT"

PAIRS = ["EURUSD", "GBPUSD", "USDJPY"]

TIMEFRAME = "3M"

SCAN_INTERVAL = 60  # seconds

# Risk settings
MAX_DAILY_LOSS = 0.1   # 10%
MAX_OPEN_TRADES = 1

# Telegram
TELEGRAM_ENABLED = True