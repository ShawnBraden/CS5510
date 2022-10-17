import math
import random
from turtle import distance
from motion import motionArm

# theta1 = −90deg, d2 = 0.5m, d3 = 1.0m, theata4 = −90deg, theta5 = 90deg, theta6 = 40deg, d6 = 0.2m
A_STARTING_DISTANCE = [1, 0.5, 1, 0, 0, 0.2]
A_STARTING_THETA = [math.radians(-90), 0, 0, math.radians(-90), math.radians(90), math.radians(40)]

# θ1 = 0deg, d2 = 0.2m, d3 = 0.3m, θ4 = −90deg, θ5 = 90deg, θ6 = 40deg, d6 = 0.2m
B_STARTING_DISTANCE = [1, 0.2, 0.3, 0, 0, 0.2]
B_STARTING_THETA = [math.radians(0), 0, 0, math.radians(-90), math.radians(90), math.radians(40)]

END_POINT = [1.2, 0.8, 0.5]
THRESHOLD = .01

def getRandom(quench, problem):
  # theta6 doesn't change so we only need to worry about 2, 4, and 5
  if problem == "c":
    theta1 = (random.random() - 0.5) * (quench * .01)
    quench = quench * .1
  else:
    theta1 = (random.random() - 0.5) * quench

  theta4 = (random.random() - 0.5) * quench
  theta5 = (random.random() - 0.5) * quench
  thetas = [theta1, theta4, theta5]

  # d2 and d3 also need to change
  if problem == "b":
    distanceQuench = quench * .01
  else:
    distanceQuench = quench

  d2 = (random.random() - 0.5) * distanceQuench
  d3 = (random.random() - 0.5) * distanceQuench
  distances = [d2, d3]

  return thetas, distances

def computeTravel(startingTheta, startingDistance, problem):
  arm = motionArm(startingDistance)
  currentPoint = arm.calculateMotionArmNotCorrected(startingTheta)
  currentTheta = startingTheta
  currentDistance = startingDistance

  n = 1000000
  for i in range(n):
    # quench this down so that we are have less variance over time
    if i < (.3 * n):
      thetaDiff, distanceDiff = getRandom(.3, problem)
    elif i < (.5 * n):
      thetaDiff, distanceDiff = getRandom(.1, problem)
    elif i < (.7 * n):
      thetaDiff, distanceDiff = getRandom(.08, problem)
    else:
      thetaDiff, distanceDiff = getRandom(.05, problem)
    
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

    if (math.dist(currentPoint, END_POINT) < THRESHOLD):
      return currentPoint, currentTheta, currentDistance


def main():
  # problem a
    finalPoint, finalThatas, finalDistances = computeTravel(A_STARTING_THETA, A_STARTING_DISTANCE, "a")
    print("Problem A")
    print("Final Point (x, y, z): ", finalPoint)
    print("Final Thetas (degrees): θ1 = %2d, θ4 = %2d, θ5 = %2d, θ6 = %2d" % (math.degrees(finalThatas[0]), math.degrees(finalThatas[3]), math.degrees(finalThatas[4]), math.degrees(finalThatas[5])))
    print("Final Distances (meters): d2 = %2f, d3 = %2f, d6 = %2f\n" % (finalDistances[1], finalDistances[2], finalDistances[5]))
    
  # problem b
    finalPoint, finalThatas, finalDistances = computeTravel(B_STARTING_THETA, B_STARTING_DISTANCE, "b")
    print("\nProblem B")
    print("Final Point (x, y, z): ", finalPoint)
    print("Final Thetas (degrees): θ1 = %2d, θ4 = %2d, θ5 = %2d, θ6 = %2d" % (math.degrees(finalThatas[0]), math.degrees(finalThatas[3]), math.degrees(finalThatas[4]), math.degrees(finalThatas[5])))
    print("Final Distances (meters): d2 = %2f, d3 = %2f, d6 = %2f\n" % (finalDistances[1], finalDistances[2], finalDistances[5]))
    

  # problem c
    finalPoint, finalThatas, finalDistances = computeTravel(B_STARTING_THETA, B_STARTING_DISTANCE, "c")
    print("\nProblem C")
    print("Final Point (x, y, z): ", finalPoint)
    print("Final Thetas (degrees): θ1 = %2d, θ4 = %2d, θ5 = %2d, θ6 = %2d" % (math.degrees(finalThatas[0]), math.degrees(finalThatas[3]), math.degrees(finalThatas[4]), math.degrees(finalThatas[5])))
    print("Final Distances (meters): d2 = %2f, d3 = %2f, d6 = %2f\n" % (finalDistances[1], finalDistances[2], finalDistances[5]))
    
main()
