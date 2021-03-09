import numpy as np


def getRange(xs, ys, xMin, xMax):
    """
    Return the Ys for the range of points where the Xs
    is at or between the given min/max limits
    """
    rangeYs = []
    for i in range(len(ys)):
        x = xs[i]
        if(x >= xMin and x <= xMax):
            rangeYs.append(ys[i])
    if len(rangeYs) == 0:
        raise Exception(f"no Y data in range {xMin} to {xMax}")
    return rangeYs


def getRangeMean(xs, ys, xMin, xMax):
    """
    Return the mean of Ys for the range of points where Xs 
    is at or between the given min/max limits.
    """
    rangeYs = getRange(xs, ys, xMin, xMax)
    return np.mean(rangeYs)


if __name__ == "__main__":

    pointCount = 100
    times = np.arange(pointCount) / 6  # simulate 10 second sweeps
    currents = np.random.rand(pointCount) * 100

    print(getRangeMean(times, currents, 3, 5))
