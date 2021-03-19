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

def getSingleSegmentSlope(segment, samplePeriod):
    """
    Return the slope of a linear line fitted to a single segment.
    Sample period must be in minutes, and returned slope will be pA/min.
    """
    xs = np.arange(len(segment)) * samplePeriod
    slope, intercept, r, p, stdErr = scipy.stats.linregress(xs, segment)
    return slope

def getAllSegmentSlopes(segments, samplePeriod):
    """
    Given a list of segments, return a list of slopes (one per segment).
    Sample period must be in minutes, and returned slopes will be pA/min.
    """
    slopes = []
    for segment in segments:
        slope = getSingleSegmentSlope(segment, samplePeriod)
        slopes.append(slope)
    return slopes

def getRegression(ys, samplePeriod):
    """
    Make linear regression during the period from xim to xmax
    This function only works on 10s sweep, and the times have to be min and starts from 0.
    xmin is included, but xmax is not included.
    """

    xs = np.arange(len(ys)) * samplePeriod
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

def consecutiveSlopes(ys, xs):
    """
    Get slopes of consecutive data points.
    """
    slopes = []
    samplePeriod  = xs[1]-xs[0]
    for i in range(len(ys)-1):
        slope = (ys[i+1]-ys[i])/(samplePeriod)
        slopes.append(slope)
    return slopes

def identifyBySlope(abfIDs, slopesDrug, slopesBaseline, threshold):
    """
    Identify a responder by comparing the change of slopes to a given threshold.
    """
    responders=[]
    nonResponders=[]
    for i in range(len(abfIDs)):

        deltaSlope = round(slopesDrug[i]-slopesBaseline[i],3)   # pA / min
        if deltaSlope> threshold:
            nonResponders.append(abfIDs[i])

        else:
            responders.append(abfIDs[i])

    return responders, nonResponders

def identifyByCurrent(abfIDs, slopesDrug, slopesBaseline,threshold):
    """
    Identify a responder by asking whether the change of current is BIGGER than a given threshold.
    """
    responders=[]
    nonResponders=[]
    for i in range(len(abfIDs)):
        deltaCurrent = round(slopesDrug[i]-slopesBaseline[i],3)   # pA / min
        if deltaCurrent > threshold:
            nonResponders.append(abfIDs[i])
        else:
            responders.append(abfIDs[i])

    return responders, nonResponders

if __name__ == "__main__":
    raise Exception("this file must be imported, not run directly")