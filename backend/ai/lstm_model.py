import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import LSTM, Dense

class LSTMModel:

    def __init__(self):

        self.model = Sequential()

        self.model.add(LSTM(50, return_sequences=True, input_shape=(10, 4)))
        self.model.add(LSTM(50))
        self.model.add(Dense(2, activation="softmax"))

        self.model.compile(
            optimizer="adam",
            loss="categorical_crossentropy",
            metrics=["accuracy"]
        )

    def prepare_data(self, df):

        X, y = [], []

        for i in range(10, len(df)):

            X.append(df[["rsi","ma_fast","ma_slow","returns"]].iloc[i-10:i].values)

            direction = 1 if df["close"].iloc[i] > df["close"].iloc[i-1] else 0
            y.append(direction)

        return np.array(X), np.array(y)

    def train(self, df):

        X, y = self.prepare_data(df)

        self.model.fit(X, y, epochs=10, batch_size=32)

    def predict(self, sequence):

        return self.model.predict(sequence)