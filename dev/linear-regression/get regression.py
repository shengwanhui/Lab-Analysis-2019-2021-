import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
import numpy as np
import os
import pyabf
thisFolder = os.path.abspath(os.path.dirname(__file__))
def getRegression(times, currents, xmin, xmax):
    index1=int(xmin*60/10)
    index2=int(xmax*60/10)
    ys = currents[index1:index2]
    xs = times[index1:index2]
    slope, intercept, r, p, stdErr = scipy.stats.linregress(xs, ys)
    return slope, intercept

slope1,intercept1 = getRegression(times, currents, baselineStartTime, baselineEndTime)
slope2,intercept2 = getRegression(times, currents, drugStartTime, drugEndTime)