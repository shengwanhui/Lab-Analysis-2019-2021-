from matplotlib.patches import FancyArrow
from numpy.lib import stride_tricks
import pyabf
import matplotlib.pyplot as plt
import numpy as np
import time

ANALYSIS_TIME_START = None
ANALYSIS_TIME = None
ANALYSIS_COUNT = 0


def getStepTrace(abf, sweepIndex: int, stepEpochIndex: int = 2, skipMsec: float = 50) -> np.array:
    """
    Return the isolated voltage trace during the depolarizing step.
    The depolarizing step is defined by the epoch number, and the first
    bit of time is trimmed to prevent analysis of the rising phase.
    """
    abf.setSweep(sweepIndex)
    stepIndex1 = abf.sweepEpochs.p1s[stepEpochIndex]
    stepIndex2 = abf.sweepEpochs.p2s[stepEpochIndex]
    skipPoints = skipMsec * abf.dataPointsPerMs
    trace = abf.sweepY[stepIndex1+skipPoints:stepIndex2]
    return trace


def plotTrace(abf: pyabf.ABF, trace: np.ndarray, newFigure: bool = True, showFigure: bool = True):
    """
    Plot an isolated trace but do not show the figure
    """
    if (newFigure):
        plt.figure(figsize=(12, 4))

    times = np.arange(len(trace)) / abf.dataRate
    plt.plot(times, trace, lw=.5)
    plt.ylabel("Potential (mV)")
    plt.xlabel("Time (seconds)")
    plt.title(abf.abfID)

    if (showFigure):
        plt.show()


def getApIndexes(trace: np.ndarray, sampleRate: float, threshold: float) -> list[int]:
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


def getInactivationTimes(abfFilePath: str, apThreshold: float = 10, minimumInactivationTime: float = .5) -> list[float]:
    """
    Return the inactivation curve for an ABF.
    The returned list is the number of seconds of inactivation by sweep.

    apThreshold: if the trace crosses this threshold (mV/ms) an AP is assumed
    minimumInactivationTime: if this number of seconds isn't reached, inactivation is assumed to be zero
    """

    global ANALYSIS_TIME_START
    if not ANALYSIS_TIME_START:
        ANALYSIS_TIME_START = time.time()

    abf = pyabf.ABF(abfFilePath)

    inactivationTimes = [0] * abf.sweepCount
    apCountBySweep = [0] * abf.sweepCount

    for sweepIndex in range(abf.sweepCount):
        trace = getStepTrace(abf, sweepIndex)
        apIndexes = getApIndexes(trace, abf.dataRate, apThreshold)
        apCountBySweep[sweepIndex] = len(apIndexes)

        if len(apIndexes) == 0:
            hasFiredInPreviousSweeps = max(apCountBySweep) > 0
            if hasFiredInPreviousSweeps:
                break  # total AP block so abort analysis
            continue

        lastApIndex = apIndexes[-1]
        lastApTime = lastApIndex / abf.dataRate
        traceEndTime = len(trace) / abf.dataRate
        inactivationTime = traceEndTime - lastApTime
        if (inactivationTime >= minimumInactivationTime):
            inactivationTimes[sweepIndex] = inactivationTime

    global ANALYSIS_TIME
    ANALYSIS_TIME = time.time() - ANALYSIS_TIME_START

    global ANALYSIS_COUNT
    ANALYSIS_COUNT += 1

    return inactivationTimes


def removeTrailingZeros(sample: list[float]) -> list[float]:
    """
    remove the last element from the array until it's no longer zero
    """
    while len(sample) and sample[-1] == 0:
        sample.pop()
    return sample


def padWith(curve: list[float], padValue: float, targetLength: int) -> list[float]:
    """
    pad the list with the given value until its length reaches the target
    """
    while(len(curve) < targetLength):
        curve.append(padValue)
    return curve


def removeEarlyInactivation(curve: list[float]) -> list[float]:
    """
    If a sweep shows inactivation but a later sweep with action potentials does not,
    zero the inactivation for this sweep. This prevents the first 1-2 sweeps with
    extremely slow firing from being misinterpreted as inactivation.
    """
    zeroSeen = False
    for i in range(len(curve))[::-1]:
        if curve[i] == 0:
            zeroSeen = True
        if zeroSeen:
            curve[i] = 0
    return curve


def curvesFromAbfs(abfPaths: list, maxTime=4, padSteps=70) -> list:
    """
    Return a list of inactivation curves for the given ABFs.

    abfPaths: list of ABF file paths
    maxTime: maximum inactivation time (applied to late sweeps with no APs)
    padSteps: pad every ABF to this number of sweeps (assuming 100% inactivation for late sweeps)
    """
    curves = []
    for abfPath in abfPaths:
        curve = getInactivationTimes(abfPath, 10)
        curve = removeTrailingZeros(curve)
        curve = padWith(curve, maxTime, padSteps)
        curve = removeEarlyInactivation(curve)
        curves.append(curve)
    return curves
