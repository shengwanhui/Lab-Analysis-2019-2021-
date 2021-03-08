"""
This module contains methods for working with ABF files
"""

import numpy as np
import pyabf

def getFirstTagTime(abfFilePath):
    """
    Return the time (in minutes) of the first tag in an ABF file
    """
    abf = pyabf.ABF(abfFilePath, False)
    if (len(abf.tagTimesMin) > 0):
        return abf.tagTimesMin[0]
    else:
        raise Exception("cannot get the first tag time because this ABF does not have any tags")
        


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
        abfID = abf.abfID
    return iHold, times, abfID

if __name__ == "__main__":
    raise Exception("this file must be imported, not run directly")