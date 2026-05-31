from stable_baselines3 import PPO
from ai.trading_env import TradingEnv

class RLAgent:

    def __init__(self, df):

        self.env = TradingEnv(df)

        self.model = PPO("MlpPolicy", self.env, verbose=0)

    def train(self):

        self.model.learn(total_timesteps=10000)

    def predict(self, obs):

        action, _ = self.model.predict(obs)
        return action