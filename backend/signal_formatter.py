from datetime import datetime, timedelta


def format_signal(pair, signal, confidence, entry_time):

    direction = "🟩 BUY" if signal == "BUY" else "🟥 SELL"

    # ⏰ STRICT parsing (no fallback guessing)
    base_time = datetime.strptime(entry_time, "%H:%M")

    # 🔥 MARTINGALE TIME LEVELS (FIXED LOGIC)
    level_1 = (base_time + timedelta(minutes=3)).strftime("%H:%M")
    level_2 = (base_time + timedelta(minutes=6)).strftime("%H:%M")
    level_3 = (base_time + timedelta(minutes=9)).strftime("%H:%M")

    return {
        "title": "🔔 NEW OTC SIGNAL!",
        "body": f"""
🎫 Trade: {pair} (OTC)

⏳ Entry Time: {entry_time}

📈 Direction: {direction}
📊 Confidence: {confidence}%

↪️ Martingale Levels:
 Level 1 → {level_1}
 Level 2 → {level_2}
 Level 3 → {level_3}
        """.strip()
    }