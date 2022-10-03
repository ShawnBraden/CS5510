from hashlib import new
import math
from motion import motionArm
import random


def computeJointAngles():
  # theta1 = −90deg, d2 = 0.5m, d3 = 1.0m, theata4 = −90deg, theta5 = 90deg, theta6 = 40deg, d6 = 0.2m
  startingD = [1, 0.5, 1, 0, 0, 0.2]
  startingTheta = [math.radians(-90), 0, 0, math.radians(-90), math.radians(90), math.radians(40)]
  endPoint = [1.2, 0.8, 0.5]
  phi = .01
  arm = motionArm(startingD)
  
  currentPoint = arm.calculateMotionArmNotCorrected(startingTheta)

  while(True):
    theta1 = random.random() * (2 * math.pi)
    theta4 = random.random() * (2 * math.pi)
    theta5 = random.random() * (2 * math.pi)
    theta6 = random.random() * (2 * math.pi)
    thetas = [theta1, 0, 0, theta4, theta5, theta6]

    newPoint = arm.calculateMotionArmNotCorrected(thetas)
    print(newPoint)

    if (math.dist(newPoint, endPoint) < math.dist(currentPoint, endPoint)):
      currentPoint = newPoint

    if (math.dist(currentPoint, endPoint) < phi):
      return thetas


def main():
  finalThatas = computeJointAngles()
  print(finalThatas)

main()
