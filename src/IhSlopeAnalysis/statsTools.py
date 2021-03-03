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





if __name__ == "__main__":
    raise Exception("this file must be imported, not run directly")