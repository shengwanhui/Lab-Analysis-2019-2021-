"""
This script demonstrates how to iterate over all files in a folder with a given extension.
This could be used to analyze every ABF in a folder.
"""

import glob

# the R before the string tells Python to ignore backslashes
filePaths = glob.glob(R"C:\Windows\system32\*.dll")
for filePath in filePaths:
    print(filePath)