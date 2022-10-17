import gym
import numpy as np

from gym import utils
from gym.envs.mujoco import MuJocoPyEnv
from gym.spaces import Box


# Part C
env = gym.make("CartPole-v1", render_mode="human")
observation, info = env.reset(seed=42)

for _ in range(1000):
    action = env.action_space.sample()
    observation, reward, terminated, truncated, info = env.step(action)

    if terminated or truncated:
        observation, info = env.reset()

# env_screen = env.render(mode = 'rgb_array')
env.close()