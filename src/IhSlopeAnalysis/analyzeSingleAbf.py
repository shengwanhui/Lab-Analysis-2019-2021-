"""
This file loads a single ABF file and plots holding current slope before/during drug exposure
"""
import pyabf
import slopeTools
import abfTools
import plotTools
import statsTools

if __name__ == "__main__":

    abfFilePaths = [R"X:/Data/C57/TGOT on PVT/2020-07-28 10nM TGOT on PVT/20804007.abf", R"X:/Data/C57/TGOT on PVT/2020-07-28 10nM TGOT on PVT/20804024.abf", R"X:/Data/C57/TGOT on PVT/2020-07-28 10nM TGOT on PVT/20804030.abf", R"X:/Data/C57/TGOT on PVT/2020-07-28 10nM TGOT on PVT/20804043.abf", R"X:/Data/C57/TGOT on PVT/2020-07-28 10nM TGOT on PVT/20804048.abf", R"X:/Data/C57/TGOT on PVT/2020-07-28 10nM TGOT on PVT/20804060.abf", R"X:/Data/C57/TGOT on PVT/2020-07-28 10nM TGOT on PVT/20804066.abf", R"X:/Data/C57/TGOT on PVT/2020-07-28 10nM TGOT on PVT/20805008.abf",R"X:/Data/C57/TGOT on PVT/2020-07-28 10nM TGOT on PVT/20805029.abf",R"X:/Data/C57/TGOT on PVT/2020-07-28 10nM TGOT on PVT/20805035.abf",R"X:/Data/C57/TGOT on PVT/2020-07-28 10nM TGOT on PVT/20811011.abf",R"X:/Data/C57/TGOT on PVT/2020-07-28 10nM TGOT on PVT/20811021.abf",R"X:/Data/C57/TGOT on PVT/2020-07-28 10nM TGOT on PVT/20817012.abf",R"X:/Data/C57/TGOT on PVT/2020-07-28 10nM TGOT on PVT/20831011.abf",R"X:/Data/C57/TGOT on PVT/2020-07-28 10nM TGOT on PVT/20831017.abf"]
    slopeBaseline=[]
    slopeDrug=[]
    for abfFilePath in abfFilePaths:
        abf = pyabf.ABF(abfFilePath)
        drugStartTime = abfTools.getFirstTagTime(abfFilePath)
        slope1, slope2 = slopeTools.plotExperiment(abfFilePath, drugStartTime, measurementTime=3, drugMeasurementDelay=1)
        slopeBaseline.append(float(slope1))
        slopeDrug.append(float(slope2))

    statsTools.pairedTTest(slopeBaseline, slopeDrug)
    plotTools.plotPairs(slopeBaseline, slopeDrug)

