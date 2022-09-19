import pandas as pd
import turtle
from motion import motion
import matplotlib.pyplot as plt

# delta t, left, right
skidCommands = [[.865, 3.54, 5.54], [1.73, 8, 10]]

# delta t, velocity, alpha
ackermanCommands = [[0.5, 8, 0.54], [2 ,8, 0.29]] # [[0.49, 8, 0.54], [1.97 ,8, 0.29]]


width = .55
length = .75


def problem1_1():
    sim = motion(skidCommands, width, length)
    sim.calculateMotionNotCorrected(.1)
    return sim.getPossitionsPredicted(), sim.getVelocityPredicted()

def problem1_2():
    sim = motion(ackermanCommands, width, length)
    sim.calculateMotionAckerman(.01)
    return sim.getPossitionsPredicted(), sim.getVelocityPredicted()

def problem1_3():
    sim = motion(ackermanCommands, width, length)
    sim.calculateForwardMotionAckerman(1)
    return sim.getPossitionsPredicted(), sim.getVelocityPredicted()

def calculateProblem1_3():
    results2 = problem1_3()

    # print("Predicted Values:")
    # for vector in results1:
    #     print(vector)
    #     t.seth(vector[2])
    #     t.goto(vector[0], vector[1])

    print("Results[0]: ", results2[0])
    print("Count: ", len(results2[0]))

    possitionsPredicted_df = pd.DataFrame(results2[0], columns=["x possitions", "y possition", "theata"])
    possitionsPredicted_df.plot(x ="x possitions", y = "y possition", kind="line", legend=None)

    # Create the data to graph the X, Y, and Theta velocities
    problem1_1X = []
    counter1 = 0
    for value in results2[1]:
        problem1_1X.append([counter1, value[0]*10])
        counter1 += .1

    problem1_1Y = []
    counter2 = 0
    for value in results2[1]:
        problem1_1Y.append([counter2, value[1]*10])
        counter2 += .1

    problem1_1Theta = []
    counter3 = 0
    for value in results2[1]:
        problem1_1Theta.append([counter3, value[2]*10])
        counter3 += .1

	# Plot the resulting path and trajectory (x, y, and angular velocities)
    twoX = pd.DataFrame(problem1_1X, columns=['X', 'Y'])
    twoX.plot(x ="X", y = "Y", kind="line", title = "Skid X Velocity", xlabel="Time (s)", ylabel="Velocity (m/s)", legend=None)
    twoY = pd.DataFrame(problem1_1Y, columns=['X', 'Y'])
    twoY.plot(x ="X", y = "Y", kind="line", title = "Skid Y Velocity", xlabel="Time (s)", ylabel="Velocity (m/s)", legend=None)
    twoTheta = pd.DataFrame(problem1_1Theta, columns=['X', 'Y'])
    twoTheta.plot(x ="X", y = "Y", kind="line", title = "Skid Theta Velocity", xlabel="Time (s)", ylabel="Velocity (rad/s)", legend=None)


def calculateProblem1_2():
    results2 = problem1_2()

    # print("Predicted Values:")
    # for vector in results1:
    #     print(vector)
    #     t.seth(vector[2])
    #     t.goto(vector[0], vector[1])

    possitionsPredicted_df = pd.DataFrame(results2[0], columns=["x possitions", "y possition", "theata"])
    possitionsPredicted_df.plot(x ="x possitions", y = "y possition", kind="line", legend=None)

    # Create the data to graph the X, Y, and Theta velocities
    problem1_1X = []
    counter1 = 0
    for value in results2[1]:
        problem1_1X.append([counter1, value[0]*10])
        counter1 += .1

    problem1_1Y = []
    counter2 = 0
    for value in results2[1]:
        problem1_1Y.append([counter2, value[1]*10])
        counter2 += .1

    problem1_1Theta = []
    counter3 = 0
    for value in results2[1]:
        problem1_1Theta.append([counter3, value[2]*10])
        counter3 += .1

    print("Theta: ", problem1_1Theta)

	# Plot the resulting path and trajectory (x, y, and angular velocities)
    twoX = pd.DataFrame(problem1_1X, columns=['X', 'Y'])
    twoX.plot(x ="X", y = "Y", kind="line", title = "Skid X Velocity", xlabel="Time (s)", ylabel="Velocity (m/s)", legend=None)
    twoY = pd.DataFrame(problem1_1Y, columns=['X', 'Y'])
    twoY.plot(x ="X", y = "Y", kind="line", title = "Skid Y Velocity", xlabel="Time (s)", ylabel="Velocity (m/s)", legend=None)
    twoTheta = pd.DataFrame(problem1_1Theta, columns=['X', 'Y'])
    twoTheta.plot(x ="X", y = "Y", kind="line", title = "Skid Theta Velocity", xlabel="Time (s)", ylabel="Velocity (rad/s)", legend=None)


def calculateProblem1_1():
    results1 = problem1_1()

    # print("Predicted Values:")
    # for vector in results1:
    #     print(vector)
    #     t.seth(vector[2])
    #     t.goto(vector[0], vector[1])

    possitionsPredicted_df = pd.DataFrame(results1[0], columns=["x possitions", "y possition", "theata"])
    possitionsPredicted_df.plot(x ="x possitions", y = "y possition", kind="line", legend=None)

    # Create the data to graph the X, Y, and Theta velocities
    problem1_1X = []
    counter1 = 0
    for value in results1[1]:
        problem1_1X.append([counter1, value[0]*10])
        counter1 += .1

    problem1_1Y = []
    counter2 = 0
    for value in results1[1]:
        problem1_1Y.append([counter2, value[1]*10])
        counter2 += .1

    problem1_1Theta = []
    counter3 = 0
    for value in results1[1]:
        problem1_1Theta.append([counter3, value[2]*10])
        counter3 += .1

    print("Theta: ", problem1_1Theta)

	# Plot the resulting path and trajectory (x, y, and angular velocities)
    twoX = pd.DataFrame(problem1_1X, columns=['X', 'Y'])
    twoX.plot(x ="X", y = "Y", kind="line", title = "Skid X Velocity", xlabel="Time (s)", ylabel="Velocity (m/s)", legend=None)
    twoY = pd.DataFrame(problem1_1Y, columns=['X', 'Y'])
    twoY.plot(x ="X", y = "Y", kind="line", title = "Skid Y Velocity", xlabel="Time (s)", ylabel="Velocity (m/s)", legend=None)
    twoTheta = pd.DataFrame(problem1_1Theta, columns=['X', 'Y'])
    twoTheta.plot(x ="X", y = "Y", kind="line", title = "Skid Theta Velocity", xlabel="Time (s)", ylabel="Velocity (rad/s)", legend=None)
	


def main():

    s = turtle.Screen()
    s.setup(1400, 1000)
    t = turtle.Turtle()

    # calculateProblem1_1()
    # calculateProblem1_2()
    calculateProblem1_3()

    plt.show()
    turtle.done()

main()
