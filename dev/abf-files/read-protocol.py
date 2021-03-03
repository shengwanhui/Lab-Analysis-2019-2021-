"""
This script demonstrates how to read the protocol from an ABF file.
This could be used to only analyze ABF files in a folder with a certain protocol.
"""

import pyabf
abfFilePath = R"X:/Data/C57/TGOT on PVT/2020-07-28 10nM TGOT on PVT/20831011.abf"
abf = pyabf.ABF(abfFilePath, loadData=False)
print(abf.protocol)