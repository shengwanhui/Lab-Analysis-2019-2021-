"""
This script inspects reversal potential of a light-induced current.
The protocol steps from +40 mV to a more negative voltage in 5 mV steps.
"""
import blsTools

abfFilePath = R"X:/Data/AT2-Cre/MPO-ChR2/abfs-pvn/2021_02_26_DIC2_0038.abf"

# location of blue light pulse determined using clampfit
# but technically could be looked-up from the ABF protocol (see pyABF tutorial)
blsStartTime = 1.07810
blsEndTime = blsStartTime + .02
viewStartTime = blsStartTime - .1
viewEndTime = blsEndTime + .1

blsTools.plotReversal(abfFilePath,
                      viewStartTime, viewEndTime,
                      blsStartTime, blsEndTime)
