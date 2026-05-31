import sqlite3
from datetime import datetime

conn = sqlite3.connect("trades.db", check_same_thread=False)
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS trades (
time TEXT,
signal TEXT,
result REAL
)
""")

def log(signal, result):

    c.execute(
        "INSERT INTO trades VALUES (?,?,?)",
        (datetime.now().isoformat(), signal, result)
    )

    conn.commit()