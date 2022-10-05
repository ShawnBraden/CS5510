import math
import random
from motion import motionArm

STARTING_D = [1, 0.5, 1, 0, 0, 0.2]
STARTING_THETA = [math.radians(-90), 0, 0, math.radians(-90), math.radians(90), math.radians(40)]
END_POINT = [1.2, 0.8, 0.5]
THRESHOLD = .001

def getRandom(quench):
  # theta6 doesn't change so we only need to worry about 2, 4, and 5
  theta1 = (random.random() - 0.5) * quench
  theta4 = (random.random() - 0.5) * quench
  theta5 = (random.random() - 0.5) * quench
  thetas = [theta1, theta4, theta5]

  # d2 and d3 also need to change
  d2 = (random.random() - 0.5) * quench
  d3 = (random.random() - 0.5) * quench
  dList = [d2, d3]

  return thetas, dList


def computeJointAngles():
  # theta1 = −90deg, d2 = 0.5m, d3 = 1.0m, theata4 = −90deg, theta5 = 90deg, theta6 = 40deg, d6 = 0.2m
  arm = motionArm(STARTING_D)
  
  currentPoint = arm.calculateMotionArmNotCorrected(STARTING_THETA)
  currentTheta = STARTING_THETA
  currentDistance = STARTING_D

  n = 100000
  for i in range(n):
    # quench this down so that we are have less variance over time
    if i < (.3 * n):
      thetaDiff, distanceDiff = getRandom(.3)
    elif i < (.5 * n):
      thetaDiff, distanceDiff = getRandom(.1)
    elif i < (.7 * n):
      thetaDiff, distanceDiff = getRandom(.08)
    else:
      thetaDiff, distanceDiff = getRandom(.05)
    
    newThetas = [
      currentTheta[0]+thetaDiff[0],
      0,
      0,
      currentTheta[3]+thetaDiff[1], 
      currentTheta[4]+thetaDiff[2], 
      currentTheta[5]
      ]
    newDistance = [1, currentDistance[1]+distanceDiff[0], currentDistance[2]+distanceDiff[1], 0, 0, 0.2]
    
    newPoint = arm.calculateMotionArmNotCorrected(newThetas, newDistance)

    if (math.dist(newPoint, END_POINT) < math.dist(currentPoint, END_POINT)):
      currentPoint = newPoint
      currentTheta = newThetas
      currentDistance = newDistance
      print("Improved Point: ", newPoint)

    if (math.dist(currentPoint, END_POINT) < THRESHOLD):
      return currentPoint, currentTheta, currentDistance
      

def main():
  finalPoint, finalThatas, finalDistances = computeJointAngles()
  print("\nFinal Point (x, y, z): ", finalPoint)
  print("Final Thetas (degrees): theta1 = %2d, theta4 = %2d, theta5 = %2d" % (math.degrees(finalThatas[0]), math.degrees(finalThatas[3]), math.degrees(finalThatas[4])))
  print("Final Distances (meters): d2 = %1f, d3 = %1f\n" % (finalDistances[1], finalDistances[2]))
  
main()
