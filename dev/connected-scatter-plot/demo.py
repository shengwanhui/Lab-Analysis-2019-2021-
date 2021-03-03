import numpy as np
import matplotlib.pyplot as plt
import scipy.stats


def plotPairs(ys1, ys2):
    """
    Display two arrays of values as a connected scatter plot
    """
    plt.figure(figsize=(3, 4))
    for i in range(len(ys1)):
        plt.plot(1, ys1[i], 'b.', ms=10)
        plt.plot(2, ys2[i], 'r.', ms=10)
        lineXs = [1, 2]
        lineYs = [ys1[i], ys2[i]]
        plt.plot(lineXs, lineYs, 'k', alpha=.5)
    
    pValue = pairedTTest(ys1, ys2)
    plt.title(f"p={pValue}")
    plt.axis([.5, 2.5, None, None])
    tickPositions = [1, 2]
    tickLabels = ["baseline", "drug"]
    plt.xticks(tickPositions, tickLabels)
    plt.show()


def pairedTTest(sample1, sample2):
    """
    Run the paired t-test and return the p value
    """
    mean1 = np.mean(sample1)
    mean2 = np.mean(sample2)
    stDev1 = np.std(sample1)
    stDev2 = np.std(sample2)
    stdErr1 = stDev1/np.sqrt(len(sample1))
    stdErr2 = stDev2/np.sqrt(len(sample2))
    tStatistic, pValue = scipy.stats.ttest_rel(sample1, sample2)
    # NOTE: for unpaired, two-sample t-test use ttest_ind()
    return pValue


if __name__ == "__main__":

    ys1 = [2, 5, 3, 4, 5, 7, 8]
    ys2 = [8, 6, 7, 5, 7, 5, 9]
    plotPairs(ys1, ys2)
    print("DONE")
