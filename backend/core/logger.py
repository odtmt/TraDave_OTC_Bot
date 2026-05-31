# backend/core/logger.py

import datetime


def log(message, level="INFO"):

    timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

    print(f"[{timestamp}] [{level}] {message}")


def log_signal(signal):

    print(f"""
━━━━━━━━━━━━━━━━━━━━
📊 SIGNAL LOG
Pair: {signal.get('pair')}
Direction: {signal.get('direction')}
Score: {signal.get('score')}
Entry: {signal.get('entry_time')}
━━━━━━━━━━━━━━━━━━━━
""")