import numpy as np
import matplotlib.pyplot as plt
import scipy.stats


def pairedTTest(sample1, sample2):
    """
    Run the paired t-test and return the p value
    """
    tStatistic, pValue = scipy.stats.ttest_rel(sample1, sample2)
    # NOTE: for unpaired, two-sample t-test use ttest_ind()
    return pValue



def descriptiveStats(sample):
    """
    Report the mean, standard deviation, standard error
    """ 
    mean = np.mean(sample)
    stDev = np.std(sample)
    stdErr = stDev/np.sqrt(len(sample))
    return mean, stDev, stdErr

def getMovingWindowSegments(data, windowSize):
    """
    Given a 1D list of data, slide a window along to create individual segments
    and return a list of lists (each of length windowSize)
    """
    segmentCount = len(data) - windowSize
    segments = [None] * segmentCount
    for i in range(segmentCount):
        segments[i] = data[i:i+windowSize]
    return segments

def rangeStats(data,start, end, outputType, interDataInterval,tagTime):
    """
    Calculate the mean, max, or min during a selected time period (min).
    """

    indexStart = int((start+(tagTime-5))/interDataInterval)
    indexEnd = int((end+(tagTime-5))/interDataInterval)
    data = data[indexStart:indexEnd]
    if outputType == "mean":
        output = sum(data)/len(data)
    elif outputType == "max":
        output = max(data)
    elif outputType == "min":
        output = min(data)
    
    else:
        print("select outputType from mean, max, min")

    return output






if __name__ == "__main__":
    raise Exception("this file must be imported, not run directly")