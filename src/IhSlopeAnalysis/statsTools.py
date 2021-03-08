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



if __name__ == "__main__":
    raise Exception("this file must be imported, not run directly")