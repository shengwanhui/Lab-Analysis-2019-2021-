"""
This file loads a single ABF file and plots holding current slope before/during drug exposure
"""

import slopeTools
import abfTools

if __name__ == "__main__":
    # the R before the string tells Python to ignore backslashes
    abfFilePath = R"X:/Data/C57/TGOT on PVT/2020-07-28 10nM TGOT on PVT/20831011.abf"
    drugStartTime = abfTools.getFirstTagTime(abfFilePath)
    slopeTools.plotExperiment(abfFilePath, drugStartTime, measurementTime=3, drugMeasurementDelay=1)