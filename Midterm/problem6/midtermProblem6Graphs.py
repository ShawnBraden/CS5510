from re import T
import pandas as pd
import matplotlib.pyplot as plt

def plotEmotions(csvLocation):
  df = pd.read_csv(csvLocation)
  df.plot(title="Emootions over time")
  plt.show()

def main():
  plotEmotions('emotionScore.csv')

main()
