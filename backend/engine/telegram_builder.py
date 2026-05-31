from backend.engine.telegram_bot import send_telegram_message


def send_signal(signal):

    message = f"""
🔔 OTC SIGNAL

📊 PAIR: {signal['pair']}
📈 DIRECTION: {signal['direction']}
⏳ TIMEFRAME: {signal['timeframe']}
🌍 SESSION: {signal['session']}
📊 SCORE: {signal['score']}
""".strip()

    send_telegram_message(message)