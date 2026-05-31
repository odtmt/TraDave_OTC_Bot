from iqoptionapi.stable_api import IQ_Option
import pandas as pd
import time
from config import EMAIL, PASSWORD, ASSET, TIMEFRAME, CANDLE_COUNT

Iq = IQ_Option(EMAIL, PASSWORD)
Iq.connect()
Iq.change_balance("PRACTICE")

def get_connection():
    return Iq

def get_data():
    candles = Iq.get_candles(ASSET, TIMEFRAME, CANDLE_COUNT, time.time())
    df = pd.DataFrame(candles).sort_values("from")

    df["close"] = df["close"].astype(float)
    return df