import random
from datetime import datetime

# 📊 MOCK MARKET DATA (replaces broken IQ Option API for now)

def get_data(symbol="EURUSD"):

    # simulate realistic price movement
    base_price = 1.1000

    price = base_price + random.uniform(-0.0100, 0.0100)

    return {
        "symbol": symbol,
        "price": round(price, 5),
        "time": datetime.utcnow().isoformat()
    }


# 🔌 OPTIONAL: placeholder for future real broker connection
def get_connection():
    return {
        "status": "mock_mode",
        "message": "Using simulated OTC data (no broker connected)"
    }