from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

@app.route("/stats")
def stats():

    conn = sqlite3.connect("trades.db")
    c = conn.cursor()

    trades = c.execute("SELECT * FROM trades").fetchall()

    wins = len([t for t in trades if t[2] and float(t[2]) > 0])
    losses = len([t for t in trades if t[2] and float(t[2]) <= 0])

    return jsonify({
        "wins": wins,
        "losses": losses,
        "total": len(trades)
    })

app.run(host="0.0.0.0", port=5000)