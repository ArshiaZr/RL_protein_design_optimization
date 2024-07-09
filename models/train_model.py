from env.protein_design_env import ProteinDesignEnv
from stable_baselines3.common.vec_env import DummyVecEnv, VecNormalize
import stable_baselines3 as sb3
import os

# Ensure the video directory exists
video_dir = "./video"
os.makedirs(video_dir, exist_ok=True)

initial_sequence = "MKTAYIAKQRQISFVKSHFSRQDILDLWIYHTQGYFPDWQNYVNVQNR"
env = ProteinDesignEnv(initial_sequence)

# Wrap the environment with DummyVecEnv for compatibility
env = DummyVecEnv([lambda: env])

# Optionally, wrap with VecNormalize
env = VecNormalize(env, norm_obs=True, norm_reward=True, clip_reward=10.0)

model = sb3.PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=10000)
model.save("data/trained_model.zip")

# To close the environment and save the video
env.close()
