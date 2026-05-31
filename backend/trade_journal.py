import json
import os

FILE = "trade_log.json"


def log_trade(data):

    if not os.path.exists(FILE):
        with open(FILE, "w") as f:
            json.dump([], f)

    with open(FILE, "r") as f:
        logs = json.load(f)

    logs.append(data)

    with open(FILE, "w") as f:
        json.dump(logs, f, indent=2)