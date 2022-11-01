import gym

# Part B
env = gym.make("CartPole-v1", render_mode="human")
observation, info = env.reset(seed=42)

# action is 0 or 1 (left or right)
action = env.action_space.sample()

for i in range(1000):  

    # determine the direction we need to move based on the pole's angle, current position and pole angular velocity
    cartPosition = observation[0]
    poleAngle = observation[2]
    poleAngularVelocity = observation[3]
    if (poleAngle > 0.15):
        action = 1
    elif (poleAngle < -0.15):
        action = 0
    # Once we are close to center start moving the other way to counteract its motion
    elif (poleAngle > -0.15 and poleAngle < 0 and action == 1):
        action = 0
    elif (poleAngle < 0.15 and poleAngle > 0 and action == 0):
        action = 1
    # Try to maintain angularVelocity as close to 0 as possible
    if (poleAngularVelocity > 0.25):
        action = 1
    elif (poleAngularVelocity < -0.25):
        action = 0
    # If we are moving too far away from center, periodically move the cart back towards the middle
    if(i % 7 == 0 and abs(cartPosition) > .1):
        action = 1 if cartPosition > 0 else 0
    observation, reward, terminated, truncated, info = env.step(action)

    print("Observation: ", observation)
    
    if terminated or truncated:
        observation, info = env.reset()
        print("\n")

env.close()
