from re import T
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('video1.csv')
df1 = pd.read_csv('video2.csv')
df.plot(title="video 1")
df1.plot(title="video 2")

plt.show()