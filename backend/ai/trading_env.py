import gym
from gym import spaces
import numpy as np

class TradingEnv(gym.Env):

    def __init__(self, df):

        super().__init__()

        self.df = df
        self.current = 0

        # actions: 0 = hold, 1 = call, 2 = put
        self.action_space = spaces.Discrete(3)

        # observation space (features)
        self.observation_space = spaces.Box(
            low=-np.inf,
            high=np.inf,
            shape=(4,),
            dtype=np.float32
        )

    def reset(self):

        self.current = 10
        return self._get_obs()

    def _get_obs(self):

        row = self.df.iloc[self.current]

        return np.array([
            row["rsi"],
            row["ma_fast"],
            row["ma_slow"],
            row["returns"]
        ], dtype=np.float32)

    def step(self, action):

        reward = 0

        current_price = self.df.iloc[self.current]["close"]
        next_price = self.df.iloc[self.current + 1]["close"]

        if action == 1 and next_price > current_price:
            reward = 1
        elif action == 2 and next_price < current_price:
            reward = 1
        elif action != 0:
            reward = -1

        self.current += 1
        done = self.current >= len(self.df) - 2

        return self._get_obs(), reward, done, {}