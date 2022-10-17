import gym
import numpy as np


# # Part C
env = gym.make("CartPole-v1", render_mode="human")
observation, info = env.reset(seed=42)

# action is 0 or 1 (left or right)
action = env.action_space.sample()

for _ in range(1000):  
  # determine the directon we need to move base on the pole's angle
    if (observation[2] > 0):  
        action = 1
    else:
        action = 0

    observation, reward, terminated, truncated, info = env.step(action)

    print("Obervation: ", observation)
    # print("Reward: ", reward)
    # print("Terminated: ", terminated)
    # print("Truncated: ", truncated)
    # print("Info: ", info)
    
    if terminated or truncated:
        observation, info = env.reset()
        # print("\n")

env.close()

class increaseRewardWrapper(gym.RewardWrapper):
    def __init__(self, env):
        super().__init__(env)
    
    def reward(self, rew):
        rew += 0.5
        return rew

class decreaseRewardWrapper(gym.RewardWrapper):
    def __init__(self, env):
        super().__init__(env)
    
    def reward(self, rew):
        rew -= 0.5
        return rew

