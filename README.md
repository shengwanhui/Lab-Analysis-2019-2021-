## Lab-Analysis
This repository is for personal projects. The source code included here is under active development and only intended for use by the original developers at this time.

## Descriptions of the jupyter nootbooks saved in src>IhSlopeAnalysis
### iHoldSegmented-regression.ipynb
The goal of this script is identifying responders based on the change of holding current slopes.
This file load a set of abf, creat segments of ach abf based on the given window size, calculate the slopes of each segment, and find the most negative slope during drug application of each cell. 

### analyzeSingleAbf.ipynb
This file load a single abf and output the slopes before and during drug application.

### analyzeAllAbf.ipynb
This file load a set of abf files and output the comparision of slopes before and during drug application.
