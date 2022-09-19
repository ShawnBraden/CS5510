import pandas as pd
import turtle
from motion import motion
import matplotlib.pyplot as plt

# delta t, left, right
circleCommands = [[.865, 3.54, 5.54], [1.73, 8, 10]]

width = .55
length = .75


def problem1_1():
    sim = motion(circleCommands, width, length)
    sim.calculateMotionNotCorrected(.1)
    return sim.getPossitionsPredicted(), sim.getVelocityPredicted()


def main():
    results1 = problem1_1()

    s = turtle.Screen()
    s.setup(1400, 1000)
    t = turtle.Turtle()

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
        problem1_1X.append([counter1, value*10])
        counter1 += .1

    problem1_1Y = []
    counter2 = 0
    for value in results1[1]:
        problem1_1Y.append([counter2, value*10])
        counter2 += .1

    problem1_1Theta = []
    counter3 = 0
    for value in results1[1]:
        problem1_1Theta.append([counter3, value*10])
        counter3 += .1

	# Plot the resulting path and trajectory (x, y, and angular velocities)
    twoX = pd.DataFrame(problem1_1X, columns=['X', 'Y'])
    twoX.plot(x ="X", y = "Y", kind="line", title = "Skid X Velocity", xlabel="Time (s)", ylabel="Velocity (m/s)", legend=None)
    twoY = pd.DataFrame(problem1_1Y, columns=['X', 'Y'])
    twoY.plot(x ="X", y = "Y", kind="line", title = "Skid Y Velocity", xlabel="Time (s)", ylabel="Velocity (m/s)", legend=None)
    twoTheta = pd.DataFrame(problem1_1Theta, columns=['X', 'Y'])
    twoTheta.plot(x ="X", y = "Y", kind="line", title = "Skid Theta Velocity", xlabel="Time (s)", ylabel="Velocity (rad/s)", legend=None)
	
    plt.show()
    turtle.done()

main()
