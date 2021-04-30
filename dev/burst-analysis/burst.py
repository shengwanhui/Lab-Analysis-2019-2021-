"""
This script identifies the time between the fist two action potentials
from a ramp protocol in order to quantify burstiness.
"""
import pyabf
import glob
import numpy as np
import matplotlib.pyplot as plt


def getListOfProtocol(protocol="0111", folderPath="X:/Data/SD/OXT-Subiculum/abfs"):
    matchingPaths = []
    for path in glob.glob(folderPath + "/*.abf"):
        abf = pyabf.ABF(path, loadData=False)
        if (abf.adcUnits[0] != "mV"):
            print("bad units: " + path)
            continue
        if abf.protocol.startswith("0111"):
            matchingPaths.append(path)
    return matchingPaths


with open("paths-all.txt") as f:
    abfPaths = f.readlines()
abfPaths = [x.strip() for x in abfPaths]
abfPaths = [x for x in abfPaths if ".abf" in x]
abfPaths = [x for x in abfPaths if not "#" in x]


def getFullTrace(abf: pyabf.ABF):
    sweeps = [None] * abf.sweepCount
    for sweepIndex in range(abf.sweepCount):
        abf.setSweep(sweepIndex)
        sweeps[sweepIndex] = abf.sweepY
    return np.concatenate(sweeps)


def getApIndexes(trace, sampleRate, threshold):
    """
    Detect action potentials using a first derivative threshold (mV/ms).
    Returns a list of indexes where each AP first crossed this threshold.
    """

    dVdt = np.diff(trace) * sampleRate / 1000  # mV/ms

    indexesAboveThreshold = np.where(dVdt >= threshold)[0]
    if (len(indexesAboveThreshold) < 5):
        return []  # no points above threshold

    apIndexes = [indexesAboveThreshold[0]]
    for i in range(1, len(indexesAboveThreshold)):
        pointsSinceLastCrossing = indexesAboveThreshold[i] - apIndexes[-1]
        if (pointsSinceLastCrossing > 100):
            apIndexes.append(indexesAboveThreshold[i])

    return apIndexes


def inspectAPs():
    plt.plot(trace)
    for apIndex in apIndexes:
        plt.axvline(apIndex, color='r')
    plt.show()


if __name__ == "__main__":
    print(f"ABF ID, # APs, First Pair Time (ms)")
    for abfPath in abfPaths:
        abf = pyabf.ABF(abfPath, False)
        if (abf.adcUnits[0] != "mV"):
            raise Exception("bad units")
        trace = getFullTrace(abf)
        apIndexes = getApIndexes(trace, abf.dataRate, 10)
        apTimesSec = [x/abf.dataRate for x in apIndexes]
        if len(apTimesSec) < 2:
            continue
        apPairTimeSec = apTimesSec[1]-apTimesSec[0]
        print(f"{abf.abfID}, {len(apTimesSec)}, {apPairTimeSec*1000:02.02f}")
