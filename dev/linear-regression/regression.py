"""
This script demonstrates how to calculate the regression line for paired X/Y data.
"""

import matplotlib.pyplot as plt
import scipy.stats
import numpy as np
import os
thisFolder = os.path.abspath(os.path.dirname(__file__))


# start with sample data
xs = [5, 15, 25, 35, 45, 55]
ys = [5, 20, 14, 32, 22, 38]

# calculate the regression
slope, intercept, r, p, stdErr = scipy.stats.linregress(xs, ys)

# create X/Y data to display as a line on the plot
fittedXs = np.linspace(0, 60)
fittedYs = fittedXs * slope + intercept

# plot the sample data and the regression line
plt.figure(figsize=(6, 3))
plt.plot(xs, ys, '.', alpha=.5, ms=20, label="data")
plt.plot(fittedXs, fittedYs, '--', label="fit")
plt.legend()
plt.title(f"Y={slope:.03f}*X + {intercept:.03f}")
imageFilePath = os.path.join(thisFolder, "regression.png")
plt.savefig(imageFilePath)
print("Saved:", imageFilePath)
plt.show()
