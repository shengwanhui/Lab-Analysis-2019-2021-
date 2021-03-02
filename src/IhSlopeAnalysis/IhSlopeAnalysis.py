import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
import numpy as np
import os
import pyabf
thisFolder = os.path.abspath(os.path.dirname(__file__))


def meanIhold(abfFilePath):
    """
    calculate the mean current for a portion of every sweep (6-10s in this case)
    """
    abf = pyabf.ABF(abfFilePath)
    sweepDuration=int(abf.protocol[29:31])
    times=[]
    iHold=[]
    for i in range(abf.sweepCount):
        abf.setSweep(i)
        pointsPerSecond = abf.dataRate
        index1 = pointsPerSecond * 6
        index2 = pointsPerSecond * 10
        segment = abf.sweepY[index1:index2]
        segmentMean = np.mean(segment)
        time=(int(i)-1)*sweepDuration/60
        times.append(time)   
        iHold.append(segmentMean)
    return iHold, times

def getRegression(times, currents, xmin, xmax):
    index1=int(xmin*60/10)
    index2=int(xmax*60/10)
    ys = currents[index1:index2]
    xs = times[index1:index2]
    slope, intercept, r, p, stdErr = scipy.stats.linregress(xs, ys)

    return slope, intercept
    

def plotExperiment(abfFilePath, drugStartTime, measurementTime):
    """
    Plot holding current for a time-course drug experiment.
    drugStartTime indicates the time (in minutes) the drug was added.
    measurementTime is the size (in minutes) of the region to fit a curve to.
    """
    
    drugEndTime = drugStartTime + measurementTime
    baselineEndTime = drugStartTime
    baselineStartTime = baselineEndTime - measurementTime

    segmentMean, t = meanIhold(abfFilePath)

    slope1,intercept1 = getRegression(t, segmentMean, baselineStartTime, baselineEndTime)
    slope2,intercept2 = getRegression(t, segmentMean, drugStartTime, drugEndTime)

    plt.figure(figsize=(8, 4))
    plt.axvspan(baselineStartTime, baselineEndTime,color="blue",alpha=0.1)
    fittedXs1 = np.linspace(baselineStartTime, baselineEndTime)
    fittedYs1 = fittedXs1 * slope1 + intercept1
    plt.plot(fittedXs1, fittedYs1, '--', label=f"slope1={slope1:0.2}", color = "blue")

    plt.axvspan(drugStartTime, drugEndTime,color="red",alpha=0.1)
    fittedXs2 = np.linspace(drugStartTime, drugEndTime)
    fittedYs2 = fittedXs2 * slope2 + intercept2
    plt.plot(fittedXs2, fittedYs2, '--', label=f"slope2={slope2:0.2}", color="red")

    plt.plot(t, segmentMean, ".", color="black", alpha=0.5,markersize=8, label="data")
    plt.title("Holding Current", fontsize=20)
    plt.ylabel("Holding Current (pA)", fontsize=12)
    plt.xlabel("Time (minutes)", fontsize=12)
    plt.grid(alpha=.2, ls='--')
    plt.legend()

    plt.show()

def getFirstTagTime(abfFilePath):
    """
    Return the time (in minutes) of the first tag in an ABF file
    """
    abf = pyabf.ABF(abfFilePath, False)
    if (len(abf.tagTimesMin) > 0):
        return abf.tagTimesMin[0]
    else:
        raise Exception("cannot get the first tag time beause this ABF does not have any tags")
        


# the R before the string tells Python to ignore backslashes
abfFilePath = R"X:/Data/C57/TGOT on PVT/2020-07-28 10nM TGOT on PVT/20831011.abf"
drugStartTime = getFirstTagTime(abfFilePath)
plotExperiment(abfFilePath, drugStartTime, 5)





