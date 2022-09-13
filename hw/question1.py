from cProfile import label
from typing import Counter
from unicodedata import name
from unittest import result
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import turtle
from turtle import width
from motion import motion

# para 1 is the duration of the command, param 2 is the speed of the left wheel and param 3 is the speed of the right wheel
h1Commands = [[5, 1, 1.5], [3, -1, -1.5], [8,0.8,-2], [10, 2, 2]]
h2Commands = [[1,5,5], [.95,1,0], [1,5,5], [.95,0,1]]
# where param 1 is deltaT, param 2 is diagobal wheel pair 1, and param 3 is diagobal wheel pair 2
h3Commands = [[1, 5, 5], [1, 1, -1], [1, 5, 5], [1, -1, 1]]
width = 0.3
length = 0.5


def problem1():
    sim = motion(h1Commands, width, length)
    sim.calculateMotionNotCorrected()

    
    return sim.getPossitionsPredicted()
    
    

def problem2():
    counter = 0 #Does this do anything? Can I delete it? -Shawn

    sim = motion(h2Commands * 9, width, length)
    sim.calculateMotionNotCorrected()

    return sim.getPossitionsPredicted()

#hw main
def main():

    results1 = problem1()

    results2 = problem2()

    s = turtle.Screen()
    s.setup(1400, 1000)
    t = turtle.Turtle()

    print("Predicted Values:")
    for vector in  results1:
        print(vector)
        t.seth(vector[2])
        t.goto(vector[0], vector[1])

    possitionsPredicted_df = pd.DataFrame(results1, columns=["x possitions", "y possition", "theata"])
    possitionsPredicted_df.plot(x ="x possitions", y = "y possition", kind="line", label = "Predicted")

    turtle.color("blue")
    turtle.penup()
    turtle.home()
    turtle.pendown()

    print("Predicted Values:")
    for vector in  results2:
        print(vector)
        t.seth(vector[2])
        t.goto(vector[0], vector[1])

    possitionsPredicted_df = pd.DataFrame(results2, columns=["x possitions", "y possition", "theata"])
    possitionsPredicted_df.plot(x ="x possitions", y = "y possition", kind="line", label = "Predicted")

    plt.show()
    turtle.done()
    

main()