import gym
from gym.envs.classic_control.cartpole import CartPoleEnv

# # Part C
env = gym.make("CartPole-v1", render_mode="human")
observation, info = env.reset(seed=42)

# action is 0 or 1 (left or right)
action = env.action_space.sample()

for _ in range(1000):  

  # determine the directon we need to move base on the pole's angle
    if (observation[2] > 0.05):  
        action = 1
    elif (observation[2] < -0.05):
        action = 0
    elif (observation[2] > -0.05 and observation[2] < 0 and action == 1):
        action = 0
    elif (observation[2] < 0.05 and observation[2] > 0 and action == 0):
        action = 1
    if(observation[3] > 0.5):
        action = 1
    elif(observation[3] < -0.5):
        action = 0

    observation, reward, terminated, truncated, info = env.step(action)

    print("Observation: ", observation)
    # print("Reward: ", reward)
    # print("Terminated: ", terminated)
    # print("Truncated: ", truncated)
    # print("Info: ", info)
    
    if terminated or truncated:
        observation, info = env.reset()
        print("\n")

env.close()
