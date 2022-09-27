import pandas as pd
import turtle
from motion import motion
import matplotlib.pyplot as plt
import math

# delta t, left, right
skidCommands = [[.865, 3.54, 5.54], [1.73, 8, 10]]

# time(seconds), velocity, alpha
ackermanCommands = [[0.5, 8, 0.54], [2 ,8, 0.29]] # [[0.49, 8, 0.54], [1.97 ,8, 0.29]]
problem1_3Commands = [[10 ,8, 0.29]]

width = .55
length = .75

velocity = 8
radius = 2.5


def problem1_1():
    sim = motion(skidCommands, width, length)
    sim.calculateMotionNotCorrected(.1)
    return sim.getPossitionsPredicted(), sim.getVelocityPredicted()

def problem1_2():
    sim = motion(ackermanCommands, width, length)
    sim.calculateMotionAckerman(.01)
    return sim.getPossitionsPredicted(), sim.getVelocityPredicted()

def problem1_3(dt):
    sim = motion(problem1_3Commands, width, length)
    sim.calculateForwardMotionAckerman(dt)
    return sim.getPossitionsPredicted()

def plotError(deltaT, resultsList):
    circumference = math.pi * 5
    errorData = []

    # Calculate the error for each point based on deltaT
    # for i in range(1, int((1 / deltaT) + 1)):
    #     theata = (((8 * deltaT) / circumference) % circumference) * (2 * math.pi)
    #     perfectPosition = motion.getCircleXYPos(2.5, theata)
    #     actualPosition = [resultsList[i-1][0], resultsList[i-1][1]]
    #     errorData.append([(i *  deltaT), math.dist(actualPosition, perfectPosition)])

    # xy = pd.DataFrame(errorData, columns=['X', 'Y'])
    # xy.plot(x ="X", y = "Y", kind="line", title = "X Error When Delta t is " + str(deltaT), xlabel="Seconds", ylabel="Error (meters)", legend=None)

    time = 1 
    perfectPositionList= []
    simPosList= []

    for simulatedPositions in resultsList:
        # arc lenght = theata * r (where theata is in radians)
        theata = (velocity * deltaT * time) / radius
        print(theata)
        perfectPosition = motion.getCircleXYPos(radius, theata)
        perfectPositionList.append(perfectPosition)
        simPosList.append(simulatedPositions[:2])
        print("Sim: ", simulatedPositions[:2], " Prefect: ", perfectPosition)
        
        
        errorData.append([(time *  deltaT), math.dist(simulatedPositions[:2], perfectPosition)])
        print("Error: ", errorData[-1])
        time += 1
    
    xy = pd.DataFrame(errorData, columns=['X', 'Y'])
    xy.plot(x ="X", y = "Y", kind="line", title = "X Error When Delta t is " + str(deltaT), xlabel="Seconds", ylabel="Error (meters)", legend=None)

    prefect = pd.DataFrame(perfectPositionList, columns=['X', 'Y'])
    prefect.plot(x ="X", y = "Y", kind="line", legend=None)

    sim = pd.DataFrame(simPosList, columns=['X', 'Y'])
    sim.plot(x ="X", y = "Y", kind="line", legend=None)
    

def calculateProblem1_3():
    results1 = problem1_3(1)
    results2 = problem1_3(.1)
    results3 = problem1_3(.01)

    plotError(1, results1)
    # plotError(.1, results2)
    # plotError(.01, results3)


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

    # calculateProblem1_1()
    # calculateProblem1_2()
    calculateProblem1_3()

    plt.show()

main()
