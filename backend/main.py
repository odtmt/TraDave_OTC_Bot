import time
import numpy as np

from data.otc_data import get_data, get_connection
from indicators.features import compute_features
from ai.lstm_model import LSTMModel
from ai.market_filter import is_good_market
from strategies.signal import get_signal
from execution.iq_executor import execute
from engine.realtime_engine import RealTimeEngine
from risk.risk_engine import can_trade, update
from logs.trade_logger import log

Iq = get_connection()
model = LSTMModel()
engine = RealTimeEngine()

while True:

    df = get_data()
    df = compute_features(df)

    if len(df) < 15:
        time.sleep(2)
        continue

    if not engine.is_new_candle(df):
        time.sleep(2)
        continue

    if not is_good_market(df):
        continue

    # last 10 candles sequence (IMPORTANT FIX)
    seq = df[["rsi","ma_fast","ma_slow","returns"]].tail(10)

    if len(seq) < 10:
        time.sleep(2)
        continue

    sequence = seq.values.reshape(1, 10, 4)

    prob = model.predict(sequence)[0]

    # convert LSTM output to same format
    signal = "CALL" if prob[1] > 0.5 else "PUT"

    print("Signal:", signal)

    if can_trade():

        result = execute(Iq, signal, "EURUSD-OTC")

        if result is not None:
            update(result)
            log(signal, result)

    time.sleep(2)