from backend.telegram_sender import send_telegram_message


def send_signal(signal):

    message = f"""
🔔 LIVE OTC SIGNAL

🌍 SESSION: {signal.get('session')}
🕒 ENTRY TIME: {signal.get('entry_time')}

📊 PAIR: {signal['pair']}
📈 DIRECTION: {signal['direction']}
⏳ TIMEFRAME: {signal['timeframe']}
📊 STRENGTH SCORE: {signal['score']}

↪️ MARTINGALE:
 L1 → +3 min
 L2 → +6 min
 L3 → +9 min

🚀 STATUS: ACTIVE SIGNAL
""".strip()

    return send_telegram_message(message)