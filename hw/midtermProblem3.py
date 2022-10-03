import math
import random
from motion import motionArm


def getRandom(tScale, d1Scale, d2Scale):
  theta1 = random.random() * tScale
  theta4 = random.random() * tScale
  theta5 = random.random() * tScale
  theta6 = random.random() * tScale
  thetas = [theta1, 0, 0, theta4, theta5, theta6]

  # d2 and d3 can change in the arm so we have to account for that here
  d2 = random.random() * d1Scale
  d3 = random.random() * d2Scale
  dList = [d2, d3]

  return thetas, dList


def computeJointAngles():
  # theta1 = −90deg, d2 = 0.5m, d3 = 1.0m, theata4 = −90deg, theta5 = 90deg, theta6 = 40deg, d6 = 0.2m
  startingD = [1, 0.5, 1, 0, 0, 0.2]
  startingTheta = [math.radians(-90), 0, 0, math.radians(-90), math.radians(90), math.radians(40)]
  endPoint = [1.2, 0.8, 0.5]
  threshold = .01
  arm = motionArm(startingD)
  
  currentPoint = arm.calculateMotionArmNotCorrected(startingTheta)

  n = 10000000
  for i in range(n):
    # quench this down so that we are have less variance over time
    if i < (.3 * n):
      thetas, dList = getRandom(.3, 5, 0.5)
    elif i < (.5 * n):
      thetas, dList = getRandom(.2, 4, 0.4)
    elif i < (.7 * n):
      thetas, dList = getRandom(.1, 3, 0.3)
    else:
      thetas, dList = getRandom(.09, 2, 0.2)

    # thetas, dList = getRandom(.3, 5, 0.5)
    
    newPoint = arm.calculateMotionArmNotCorrected(thetas, dList)

    if (math.dist(newPoint, endPoint) < math.dist(currentPoint, endPoint)):
      currentPoint = newPoint
      print("Improved Point: ", newPoint)

    if (math.dist(currentPoint, endPoint) < threshold):
      return thetas
      

def main():
  finalThatas = computeJointAngles()
  print("Final Thetas: ", finalThatas)
  
main()
