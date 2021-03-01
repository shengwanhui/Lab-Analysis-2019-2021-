import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
import numpy as np
import os
thisFolder = os.path.abspath(os.path.dirname(__file__))

file="../../data/20817006.abf.csv"
csvData = pd.read_csv(file,sep=",",skiprows=2) # read all the data except the title and unit rows

times = csvData.iloc[:,0] # ,iloc[:,0] means all rows from the first column

currents = csvData.iloc[:,1] # .iloc[:,1] means all rows from the second column
print("currents")

# plot current-over-time figure
plt.figure(figsize=(8, 4))
plt.plot(times, currents, ".-")
plt.title("Holding Current", fontsize=20)
plt.ylabel("Holding Current (pA)", fontsize=12)
plt.xlabel("Time (minutes)", fontsize=12)
plt.grid(alpha=.2, ls='--')

plt.savefig("Ihold.png")
#plt.show()

# calculate the slope every 5 sweeps
dIdt = []
duration = []
for t in times:
    x = 2.5
    t = csvData.iloc[x-2.5:x+2.5,0]
    I = csvData.iloc[x-2.5:x+2.5,1]
    slope, intercept, r, p, stdErr = scipy.stats.linregress(t, I)
    dIdt.append(slope)
    duration.append(x)
    x = x+5

# plot the sample data and the regression line
plt.figure(figsize=(6, 3))
plt.plot(duration, dIdt, '.', alpha=.5, ms=20, label="slope")
#plt.plot(fittedXs, fittedYs, '--', label="fit")
plt.legend()
plt.title(f"change of slope over time")
imageFilePath = os.path.join(thisFolder, "slope.png")
plt.savefig(imageFilePath)
print("Saved:", imageFilePath)
plt.show()


fittedXs = np.linspace(0, 60)   # Return evenly spaced numbers over a specified interval.



