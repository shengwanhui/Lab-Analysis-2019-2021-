## Lab-Analysis
This repository is for personal projects. The source code included here is under active development and only intended for use by the original developers at this time.

## Descriptions of the jupyter nootbooks saved in src>IhSlopeAnalysis
### [analyzeRangeAvgSlope.ipynb](/notebooks/analyzeRangeAvgSlope.ipynb)
The goal of this script The goal of this script is identifying responders based on the change of holding current slopes.

This file loads a set of abf, generates smoothed holding current by averaging adjacent data points, and calculates the consecutive slope with the smoothed data. The most negative slope was identified.
![](/doc/examples/rangeAvgSlope.png)

### [iHoldSegmented-regression.ipynb](/notebooks/iHoldSegmented-regression.ipynb)
The goal of this script is identifying responders based on the change of holding current slopes.

This file loads a set of abf, creates segments of ach abf based on the given window size, calculates the slopes of each segment, and finds the most negative slope during drug application of each cell. 
![](/doc/examples/Segmented-regression.png)

### [analyzeSingleAbf.ipynb](/notebooks/analyzeSingleAbf.ipynb)
This file load a single abf and output the slopes before and during drug application.

### [analyzeAllAbf.ipynb](/notebooks/analyzeAllAbf.ipynb)
This file load a set of abf files and output the comparison of slopes before and during drug application.
