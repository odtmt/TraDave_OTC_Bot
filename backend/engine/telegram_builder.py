from backend.engine.telegram_bot import send_telegram_message


def send_signal(signal):

    martingale_text = "\n".join([
        f" L{m['level']} → {m['time']}"
        for m in signal.get("martingale", [])
    ])

    message = f"""
🔔 OTC SIGNAL

📊 PAIR: {signal['pair']}
📈 DIRECTION: {signal['direction']}
⏳ TIMEFRAME: {signal['timeframe']}
🌍 SESSION: {signal['session']}
📊 SCORE: {signal['score']}

🕒 ENTRY TIME: {signal.get('entry_time', 'N/A')}

↪️ MARTINGALE:
{martingale_text if martingale_text else "No martingale data"}
""".strip()

    return send_telegram_message(message)