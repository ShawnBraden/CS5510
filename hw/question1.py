import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import turtle
from motion import motion
from enum import Enum

# param 1 is the duration of the command, param 2 is the speed of the left wheel and param 3 is the speed of the right wheel
h1Commands = [[5, 1, 1.5], [3, -1, -1.5], [8,0.8,-2], [10, 2, 2]]
h2Commands = [[1,5,5], [.95,1,0], [1,5,5], [.95,0,1]]

width = 0.3
length = 0.5

swedishData = [
    [0,0,0], [0,5,0], [.3,5,0], [.3,0,0], 
    [.6,0,0], [.6,5,0], [.9,5,0], [.9,0,0],
    [1.2,0,0], [1.2,5,0], [1.5,5,0], [1.5,0,0],
    [1.8,0,0], [1.8,5,0], [2.1,5,0], [2.1,0,0],
    [2.4,0,0], [2.4,5,0], [2.7,5,0], [2.7,0,0],
    [3,0,0], [3,5,0], [3.3,5,0], [3.3,0,0],
    [3.6,0,0], [3.6,5,0], [3.9,5,0], [3.9,0,0],
    [4.2,0,0], [4.2,5,0], [4.5,5,0], [4.5,0,0],
    [4.8,0,0], [4.8,5,0], [5.1,5,0], [5.1,0,0], [5.4,0,0]
]

swedishDataX = [
    [1, 0], [2, 0], [3, .3,], [4, .3],
    [5, .6], [6, .6], [7, .9,], [8, .9],
    [9, 1.2], [10, 1.2], [11, 1.5,], [12, 1.5],
    [13, 1.8], [14, 1.8], [15, 2.1,], [16, 2.1],
    [17, 2.4], [18, 2.4], [19, 2.7,], [20, 2.7],
    [21, 3], [22, 3], [23, 3.3,], [24, 3.3],
    [25, 3.6], [26, 3.6], [27, 3.9,], [28, 3.9],
    [29, 4.2], [30, 4.2], [31, 4.5,], [32, 4.5],
    [33, 4.8], [34, 4.8], [35, 5.1,], [36, 5.1], [37, 5.4]   
]

swedishDataY = [
    [1, 0], [2, 5], [3, 5], [4,0],
    [5, 0], [6, 5], [7, 5], [8,0],
    [9, 0], [10, 5], [11, 5], [12,0],
    [13, 0], [14, 5], [15, 5], [16,0],
    [17, 0], [18, 5], [19, 5], [20,0],
    [21, 0], [22, 5], [23, 5], [24,0],
    [25, 0], [26, 5], [27, 5], [28,0],
    [29, 0], [30, 5], [31, 5], [32,0],
    [33, 0], [34, 5], [35, 5], [36,0], [37, 0]
]

swedishDataTheta = [
    [1,0], [2, 0], [3, 0], [4, 0],
    [5, 0], [6, 0], [7, 0], [8, 0],
    [9, 0], [10, 0], [11, 0], [12, 0],
    [13, 0], [14, 0], [15, 0], [16, 0],
    [17, 0], [18, 0], [19, 0], [20, 0],
    [21, 0], [22, 0], [23, 0], [24, 0],
    [25, 0], [26, 0], [27, 0], [28, 0],
    [29, 0], [30, 0], [31, 0], [32, 0],
    [33, 0], [34, 0], [35, 0], [36, 0], [37, 0]
]


def problem1():
    sim = motion(h1Commands, width, length)
    sim.calculateMotionNotCorrected(.1)
    return sim.getPossitionsPredicted()
    
def problem2():
    sim = motion(h2Commands * 9, width, length)
    sim.calculateMotionNotCorrected(.01)
    return sim.getPossitionsPredicted()

def main():

    # Used to test individual problems. Not needed for final submission
    firstProblem = True
    secondProblem = True
    thirdProblem = True

    results1 = problem1()
    results2 = problem2()

    s = turtle.Screen()
    s.setup(1400, 1000)
    t = turtle.Turtle()

    # Problem 1
    if firstProblem:
        # print("Predicted Values:")
        # for vector in results1:
        #     print(vector)
        #     t.seth(vector[2])
        #     t.goto(vector[0], vector[1])

        possitionsPredicted_df = pd.DataFrame(results1, columns=["x possitions", "y possition", "theata"])
        possitionsPredicted_df.plot(x ="x possitions", y = "y possition", kind="line", label = "Predicted")

    # Problem 2
    if secondProblem:
        t.color("blue")
        t.penup()
        t.home()
        changeProblem = True

        # print("Predicted Values:")
        # for vector in results2:
        #     print(vector)
        #     t.seth(vector[2])
        #     t.goto(vector[0], vector[1])

        #     if changeProblem:
        #         t.pendown()
        #         changeProblem = False

        possitionsPredicted_df = pd.DataFrame(results2, columns=["x possitions", "y possition", "theata"])
        possitionsPredicted_df.plot(x ="x possitions", y = "y possition", kind="line", label = "Predicted")

        # Create the data to graph the X, Y, and Theta velocities for problem 2   
        problem2X = []
        counter = 0
        for value in results2:
            problem2X.append([counter + 1, value[0]])
            counter += 1

        problem2Y = []
        counter = 0
        for value in results2:
            problem2Y.append([counter + 1, value[1]])
            counter += 1

        problem2Theta = []
        counter = 0
        for value in results2:
            problem2Theta.append([counter + 1, value[2]])
            counter += 1
    
        # Plot the resulting path (x, y) and trajectory (x, y, and angular velocities)
        twoX = pd.DataFrame(problem2X, columns=['X', 'Y'])
        twoX.plot(x ="X", y = "Y", kind="line", title = "Skid X Velocity")
        twoY = pd.DataFrame(problem2Y, columns=['X', 'Y'])
        twoY.plot(x ="X", y = "Y", kind="line", title = "Skid Y Velocity")
        twoTheta = pd.DataFrame(problem2Theta, columns=['X', 'Y'])
        twoTheta.plot(x ="X", y = "Y", kind="line", title = "Skid Theta Velocity")     

    # Problem 3
    if thirdProblem:
        t.color("green")
        t.penup()
        t.home()
        changeProblem = True

        print("Predicted Values:")

        # for vector in swedishData:
        #     print(vector)
        #     t.seth(vector[2])
        #     t.goto(vector[0], vector[1])

        #     if changeProblem:
        #         t.pendown()
        #         changeProblem = False

        dfEverything = pd.DataFrame(swedishData, columns=['X', 'Y', 'Angle'])
        dfEverything.plot(x ="X", y = "Y", kind="line", title = "Swedish Wheels", legend=None)

        # Plot the resulting path (x, y) and trajectory (x, y, and angular velocities)
        threeX = pd.DataFrame(swedishDataX, columns=['X', 'Y'])
        threeX.plot(x ="X", y = "Y", kind="line", title = "Swedish X Velocity", legend=None)
        threeY = pd.DataFrame(swedishDataY, columns=['X', 'Y'])
        threeY.plot(x ="X", y = "Y", kind="line", title = "Swedish Y Velocity", legend=None)
        threeTheta = pd.DataFrame(swedishDataTheta, columns=['X', 'Y'])
        threeTheta.plot(x ="X", y = "Y", kind="line", title = "Swedish Theta Velocity", legend=None)      

    plt.show()
    turtle.done()

main()