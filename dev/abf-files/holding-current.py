"""
This script demonstrates how to read holding current from ABF files.
You may need to install pyABF using the command "pip install pyabf"
"""

import pyabf
import numpy as np

# the R before the string tells Python to ignore backslashes
abfFilePath = R"C:\Users\scott\Documents\GitHub\pyABF\data\abfs\2019_05_02_DIC2_0011.abf"

abf = pyabf.ABF(abfFilePath)

# Let's calculate the mean current for a portion of every sweep (2-5 seconds)
for i in range(abf.sweepCount):
    abf.setSweep(i)
    pointsPerSecond = abf.dataRate
    index1 = pointsPerSecond * 2
    index2 = pointsPerSecond * 5
    segment = abf.sweepY[index1:index2]
    segmentMean = np.mean(segment)
    print(f"sweep {i} mean current = {segmentMean} pA")
