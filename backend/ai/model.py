import numpy as np
from sklearn.ensemble import RandomForestClassifier

class MLModel:

    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=150)

    def train(self, df):

        df = df.copy()
        df["target"] = (df["close"].shift(-1) > df["close"]).astype(int)

        X = df[["rsi","ma_fast","ma_slow","returns"]]
        y = df["target"]

        self.model.fit(X, y)

    def predict(self, row):

        x = np.array(row[["rsi","ma_fast","ma_slow","returns"]]).reshape(1,-1)
        return self.model.predict_proba(x)[0]