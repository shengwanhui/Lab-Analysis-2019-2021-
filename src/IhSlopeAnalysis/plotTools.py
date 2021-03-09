import matplotlib.pyplot as plt
import statsTools
import abfTools
import numpy as np
import os

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
    
    pValue = statsTools.pairedTTest(ys1, ys2)
    plt.title(f"p={pValue}")
    plt.axis([.5, 2.5, None, None])
    tickPositions = [1, 2]
    tickLabels = ["baseline", "drug"]
    plt.xticks(tickPositions, tickLabels)
    plt.show()

def plotTwoGroups(ys1, ys2):
    plt.figure(figsize=(3, 4))
    for i in range(len(ys1)):
        plt.plot(1, ys1[i], 'b.', ms=10)
    for i in range(len(ys2)):
        plt.plot(2, ys2[i], 'r.', ms=10)
    # NOTE: for unpaired, two-sample t-test use ttest_ind()
    plt.axis([.5, 2.5, None, None])
    tickPositions = [1, 2]
    tickLabels = ["responders", "non-res"]
    plt.xticks(tickPositions, tickLabels)
    plt.show()    

def scatterPlot(xs, ys, abfFilePath, yAxisLabel):
    plt.figure(figsize=(8, 4))
    tagTime = abfTools.getFirstTagTime(abfFilePath)
    xs = np.array(xs) - tagTime
   
    plt.plot(xs, ys, '.-', color = "blue", alpha = 0.2)
    plt.xlabel("Time (minutes)")
    plt.ylabel(yAxisLabel)
    plt.xlim(0,None)
    plt.show()

def currentSlopeTimePlot(currents, timesRaw, slopes,timesSegs,peakSlopeTime, peakSlopeValue, windowSize, sweepPeriod, abfFilePath):
    ax1 = plt.subplot(211)
    #plt.xlim(0,None)
    plt.axvspan(5, 10, color = "yellow", alpha = .2) # drug application time (5-10min)
    plt.plot(timesRaw, currents, '.-')
    plt.xlabel("Time (minutes)")
    plt.ylabel("Current (pA)")
    plt.axvline(peakSlopeTime, ls='--', color='r', lw=1, alpha=.2)
    # add abf name to the title
    abfName = os.path.basename(abfFilePath)
    plt.title(abfName, fontsize=20)

    # highlight the window around the peak neagtive slope
    halfWindowTime = (windowSize * sweepPeriod) / 2
    plt.axvspan(peakSlopeTime - halfWindowTime, peakSlopeTime + halfWindowTime, color='r', alpha=.2) # the segment used for slope max

    ax2 = plt.subplot(212, sharex=ax1)
    plt.axvspan(5, 10, color = "yellow", alpha = .2)  # drug application time (5-10min)
    plt.plot(timesSegs, slopes, '.-', color = "green")
    plt.plot(peakSlopeTime, peakSlopeValue, 'r.', ms=15, alpha=.5)
    plt.xlabel("Time (minutes)")
    plt.ylabel("Slope (pA / min)")
    plt.axhline(0, ls='--', color='k', lw=1, alpha=.2)
    plt.axvline(peakSlopeTime, ls='--', color='r', lw=1, alpha=.2)
    plt.show()


def plotExperimentFromCSV(csvFilePath, baselineStartTime, baselineEndTime, drugStartTime, drugEndTime):
    csvData = pd.read_csv(csvFilePath, sep=",", skiprows=2)
    times = csvData.iloc[:,0] # ,iloc[:,0] means all rows from the first column
    currents = csvData.iloc[:,1]

    slope1,intercept1 = getRegression(times, currents, baselineStartTime, baselineEndTime)
    slope2,intercept2 = getRegression(times, currents, drugStartTime, drugEndTime)

    plt.figure(figsize=(8, 4))
    plt.axvspan(baselineStartTime, baselineEndTime,color="blue",alpha=0.1)
    fittedXs1 = np.linspace(baselineStartTime, baselineEndTime)
    fittedYs1 = fittedXs1 * slope1 + intercept1
    plt.plot(fittedXs1, fittedYs1, '--', label=f"slope1={slope1:0.2}", color = "blue")

    plt.axvspan(drugStartTime, drugEndTime,color="red",alpha=0.1)
    fittedXs2 = np.linspace(drugStartTime, drugEndTime)
    fittedYs2 = fittedXs2 * slope2 + intercept2
    plt.plot(fittedXs2, fittedYs2, '--', label=f"slope2={slope2:0.2}", color="red")

    plt.plot(times, currents, ".", color="black", alpha=0.5,markersize=8, label="data")
    plt.title("Holding Current", fontsize=20)
    plt.ylabel("Holding Current (pA)", fontsize=12)
    plt.xlabel("Time (minutes)", fontsize=12)
    plt.grid(alpha=.2, ls='--')
    plt.legend()

    plt.show()

    
if __name__ == "__main__":
    raise Exception("this file must be imported, not run directly")