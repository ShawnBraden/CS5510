from cProfile import label
import math
from unicodedata import name
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import turtle

commands = [[5, 1, 1.5], [3, -1, -1.5], [8,0.8,-2], [10, 2, 2]]
width = 0.3
length = 0.5
width_i = 1 / width
widthAvg = width / 2

possitionsPredicted = []
possitionsCorrected = []

def motionSkidSteerPredicted(deltaT, V_left, V_right, x, y, theata):
    x_now = x - (0.5 * (V_right + V_left) * math.degrees(math.sin(theata)) * deltaT)
    y_now = y + (0.5 * (V_right + V_left) * math.degrees(math.cos(theata)) * deltaT)
    theata_Now = theata + (width_i * (V_right + V_left) * deltaT)
    return [x_now, y_now, theata_Now]

def motionSkidSteerPredictedCorrected(V_left, V_right, x, y):
    try :
        r = widthAvg * ((V_right + V_left) / (V_right - V_left))
    except :
        return [x, y]
    c = 2 * math.pi * r
    theataError = 360 * (y / c)
    yCorrected = math.degrees(math.sin(theataError)) * r
    xCorrected = math.degrees(math.cos(theataError)) * r
    return [yCorrected, xCorrected]

def calculateMotion():
    currentx = 0
    currenty = 0
    currentTheata = 0
    for vector in commands:
        possitionsPredicted.append(motionSkidSteerPredicted(vector[0], vector[1], vector[2], currentx, currenty, currentTheata))
        possitionsCorrected.append(motionSkidSteerPredictedCorrected(vector[1], vector[2], possitionsPredicted[-1][0], possitionsPredicted[-1][1]))
        currentx = possitionsCorrected[-1][0]
        currenty = possitionsCorrected[-1][1]
        currentTheata = possitionsPredicted[-1][2]

def main():
    calculateMotion()

    s = turtle.getscreen()
    t = turtle.Turtle()

    print("Predicted Values:")
    for vector in  possitionsPredicted:
        print(vector)
        t.seth(vector[2])
        t.goto(vector[0], vector[1])
    print("Corrected Values:")
    for vector in possitionsCorrected:
        print(vector)
        t.home()
        t.color("blue")
        t.goto(vector[0], vector[1])


    possitionsPredicted_df = pd.DataFrame(possitionsPredicted, columns=["x possitions", "y possition", "theata"])
    possitionsPredicted_df.plot(x ="x possitions", y = "y possition", kind="line", label = "Predicted")
    possitionsCorrected_df = pd.DataFrame(possitionsCorrected, columns=["x possitions", "y possition"])
    possitionsCorrected_df.plot(x ="x possitions", y = "y possition", kind="line", label = "Corrected")

    plt.show()

    




main()