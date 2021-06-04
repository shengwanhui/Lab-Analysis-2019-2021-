import pyabf
import matplotlib.pyplot as plt
import numpy as np


def highlightInactivation(abfPath: str,
                      derivative: bool = False,
                      inactivationTimes: list = None):
    """
    Plot every sweep of an ABF and highlight portions of the trace
    likely to represent action potentials.

    If derivative is not used, voltages >=0 mV are highlighted.

    If derivative is not used, voltage changes >=10mV/ms are highlighted.
    """
    abf = pyabf.ABF(abfPath)
    plt.gca().get_yaxis().set_visible(False)
    plt.title(f"{abf.abfID} (dV/dt)" if derivative else f"{abf.abfID} (V)")
    plt.xlabel("Step Time (sec)")
    stepIndexes = [abf.sweepEpochs.p1s[2], abf.sweepEpochs.p2s[2]]

    for sweepIndex in abf.sweepList:
        abf.setSweep(sweepIndex)
        ys = abf.sweepY[stepIndexes[0]:stepIndexes[1]]
        xs = abf.sweepX[:len(ys)]

        if (derivative):
            dYdt = np.diff(ys) * (abf.dataRate / 1000)  # ms/ms units
            yOffset = sweepIndex * 100
            plt.plot(xs[1:], dYdt + yOffset, 'r-', alpha=.2)
            indexesInactive = np.argwhere(np.abs(dYdt) < 10)
            highlighted = np.array(dYdt)
            highlighted[indexesInactive] = np.nan
            plt.plot(xs[1:], highlighted + yOffset, 'r-')

        else:
            yOffset = sweepIndex * 50
            plt.plot(xs, ys + yOffset, 'b-', alpha=.2)
            indexesInactive = np.argwhere(ys < 0)
            highlighted = np.array(ys)
            highlighted[indexesInactive] = np.nan
            plt.plot(xs, highlighted + yOffset, 'b-')

            if (inactivationTimes):
                firstInactivatedPoint = len(xs) -\
                    int(abf.dataRate * inactivationTimes[sweepIndex])
                plt.plot(xs[firstInactivatedPoint:],
                         ys[firstInactivatedPoint:] + yOffset,
                         'r-', alpha=.5, lw=5)


def highlightInactivation3(abfPath: str, inactivationTimes: list = None, show = False, saveAs = None):
    """
    Create a 2-panel figure highlighting V and dV/dt from every trace.
    """
    plt.figure(figsize=(15, 4))
    plt.subplot(131)
    highlightInactivation(abfPath, False, inactivationTimes)
    plt.subplot(132)
    highlightInactivation(abfPath, True, inactivationTimes)
    plt.subplot(133)
    currents = np.arange(len(inactivationTimes)) * 20 - 100
    plt.plot(currents, inactivationTimes, '.-')
    plt.grid(alpha=.5, ls='--')
    plt.title("Inactivation Curve")
    plt.ylabel("Inactivation (sec)")
    plt.xlabel("Applied Current (pA)")
    if show:
        plt.show()
    if saveAs:
        plt.savefig(saveAs)