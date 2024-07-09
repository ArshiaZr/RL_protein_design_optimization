import gym
import numpy as np
from gym import spaces

class ProteinDesignEnv(gym.Env):
    def __init__(self, sequence):
        super(ProteinDesignEnv, self).__init__()
        self.sequence = sequence
        self.action_space = spaces.Discrete(20)  # 20 amino acids to choose from
        self.observation_space = spaces.Box(low=0, high=1, shape=(960,), dtype=np.float32)  # Assuming a flattened one-hot encoding of length 960
        self.max_steps = 1000  # Example: Set a maximum number of steps

    def reset(self):
        self.current_step = 0
        self.current_sequence = self.sequence[:]
        return self._get_observation()

    def step(self, action):
        index = np.random.randint(0, len(self.current_sequence))
        new_amino_acid = chr(action + 65)  # Convert action to corresponding amino acid
        self.current_sequence = self.current_sequence[:index] + new_amino_acid + self.current_sequence[index+1:]
        obs = self._get_observation()
        reward = self._calculate_reward()
        done = self.current_step >= self.max_steps  # Use self.max_steps for termination condition
        info = {}  # Additional info if needed
        self.current_step += 1
        return obs, reward, done, info

    def _get_observation(self):
        obs = np.zeros((len(self.sequence), 20), dtype=np.float32)
        for i, amino_acid in enumerate(self.current_sequence):
            if amino_acid.isalpha() and amino_acid.isupper() and ord(amino_acid) - 65 < 20:
                obs[i, ord(amino_acid) - 65] = 1.0  # Set corresponding index to 1
        return obs.flatten()  # Flatten to a 1D array

    def _calculate_reward(self):
        # Implement your own reward calculation logic here
        return 0.0  # Placeholder reward

    def render(self, mode='human'):
        # Optional: Implement visualization of the environment state
        pass
