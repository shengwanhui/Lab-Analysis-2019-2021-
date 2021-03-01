#print("How hard can Python be?")

import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
import numpy as np
import os
thisFolder = os.path.abspath(os.path.dirname(__file__))

def getRegression(times, currents, xmin, xmax):
    index1=int(xmin*60/10)
    index2=int(xmax*60/10)
    ys = currents[index1:index2]
    xs = times[index1:index2]
    slope, intercept, r, p, stdErr = scipy.stats.linregress(xs, ys)
    return slope, intercept

file = os.path.join(thisFolder, "../data/20817006.abf.csv")
csvData = pd.read_csv(file,sep=",",skiprows=2)
times = csvData.iloc[:,0] # ,iloc[:,0] means all rows from the first column
currents = csvData.iloc[:,1]

baselineStartTime=0
baselineEndTime =5
drugStartTime=5
drugEndTime=10
slope1,intercept1 = getRegression(times, currents, baselineStartTime, baselineEndTime)
slope2,intercept2 = getRegression(times, currents, drugStartTime, drugEndTime)
print(slope1, intercept1)
print(slope2, intercept2)

plt.figure(figsize=(8, 4))
plt.axvspan(baselineStartTime, baselineEndTime,color="blue",alpha=0.1)
fittedXs1 = np.linspace(baselineStartTime, baselineEndTime)
fittedYs1 = fittedXs1 * slope1 + intercept1
plt.plot(fittedXs1, fittedYs1, '--', label=f"slope1={slope1:0.2}", color = "blue")

plt.axvspan(drugStartTime, drugEndTime,color="red",alpha=0.1)
fittedXs2 = np.linspace(drugStartTime, drugEndTime)
fittedYs2 = fittedXs2 * slope2 + intercept2
plt.plot(fittedXs2, fittedYs2, '--', label=f"slope2={slope2:0.2}", color="red")


plt.plot(times, currents, ".", color="black", alpha=0.5,markersize=8, label="data")
plt.title("Holding Current", fontsize=20)
plt.ylabel("Holding Current (pA)", fontsize=12)
plt.xlabel("Time (minutes)", fontsize=12)
plt.grid(alpha=.2, ls='--')
plt.legend()






plt.show()