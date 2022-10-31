import math
 
def getTotalDistance(path):
  totalDistance = 0
  for i in range(len(path)-1):
    distance = abs(math.dist(path[i], path[i+1]))
    totalDistance += distance

  return totalDistance

def printResults(totalDistance, totalTime):
  print(f"Average Time: {totalTime / 10 : 0.8f}")
  print(f"Average Length: {totalDistance/10 : 0.4f}\n")
