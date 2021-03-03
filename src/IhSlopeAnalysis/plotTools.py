import matplotlib.pyplot as plt
import statsTools

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

    
if __name__ == "__main__":
    raise Exception("this file must be imported, not run directly")