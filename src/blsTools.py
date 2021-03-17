import pyabf
import pyabf.filter
import matplotlib.pyplot as plt


def plotReversal(abfFilePath, viewStart, viewEnd, blsStart, blsEnd):
    """
    Plot every sweep of an ABF stacked on top of each other,
    shade the region of BLS in blue,
    and label the voltage for every sweep.
    """
    
    abf = pyabf.ABF(abfFilePath)

    # apply a gaussian lowpass filter to all the sweeps
    pyabf.filter.gaussian(abf, .2)

    # determine where the baseline should be. Let's do 50ms before the light.
    baselineTime2 = blsStart
    baselineTime1 = baselineTime2 - .050

    plt.figure(figsize=(8, 8))
    plt.axvspan(blsStart, blsEnd, color='b', alpha=.1)

    for sweepNumber in range(abf.sweepCount):
        clampVoltage = 40 - 5 * sweepNumber
        abf.setSweep(sweepNumber, baseline=[baselineTime1, baselineTime2])
        yOffset = - sweepNumber * 40
        plt.plot(abf.sweepX, abf.sweepY + yOffset, '-', lw=1, color='C0')
        plt.text(viewStart, yOffset + 5, f"{clampVoltage} mV", fontsize=6)

    plt.axis([viewStart, viewEnd, None, None])
    plt.gca().axis('off')
    plt.show()
