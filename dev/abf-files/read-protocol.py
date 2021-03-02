"""
This script demonstrates how to read the protocol from an ABF file.
This could be used to only analyze ABF files in a folder with a certain protocol.
"""

import pyabf
abfFilePath = R"C:\Users\scott\Documents\GitHub\pyABF\data\abfs\2019_05_02_DIC2_0011.abf"
abf = pyabf.ABF(abfFilePath, loadData=False)
print(abf.protocol)