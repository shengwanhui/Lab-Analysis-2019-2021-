"""
Slope tools contains helper functions for measuring slow changes in holding current
using linear regressions. 
"""

import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
import numpy as np
import os
import pyabf
import abfTools

def getRegression(times, currents, xmin, xmax):
    index1=int(xmin*60/10)
    index2=int(xmax*60/10)
    ys = currents[index1:index2]
    xs = times[index1:index2]
    slope, intercept, r, p, stdErr = scipy.stats.linregress(xs, ys)

    return slope, intercept
    

def plotExperiment(abfFilePath, drugStartTime, measurementTime, drugMeasurementDelay):
    """
    Plot holding current for a time-course drug experiment.
    drugStartTime indicates the time (in minutes) the drug was added.
    measurementTime is the size (in minutes) of the region to fit a curve to.
    """
    
    # figure out the drug end time and baseline times based on the drug start time
    drugEndTime = drugStartTime + measurementTime
    baselineEndTime = drugStartTime
    baselineStartTime = baselineEndTime - measurementTime

    # shift the drug measurement region to the right by the drug measurement delay
    drugStartTime = drugStartTime + drugMeasurementDelay
    drugEndTime = drugEndTime + drugMeasurementDelay

    segmentMean, t = abfTools.meanIhold(abfFilePath)

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
    abfName = os.path.basename(abfFilePath)
    plt.title(abfName, fontsize=20)
    plt.ylabel("Holding Current (pA)", fontsize=12)
    plt.xlabel("Time (minutes)", fontsize=12)
    plt.grid(alpha=.2, ls='--')
    plt.legend()

    #plt.show()
    return round(slope1,3), round(slope2,3)


if __name__ == "__main__":
    raise Exception("this file must be imported, not run directly")