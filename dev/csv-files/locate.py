"""
Demo: locate a CSV file when you don't know what folder Python is launched from

When a python script looks for a file (like a CSV file), it looks in the same folder
that python.exe was launched from. This makes files hard to find sometimes when
python scripts are launched from other folders, or launched from other python scripts.
This also makes it hard to save files (like plots as images) into a specific folder.

This script demonstrates how to determine what folder this python script lives in, 
and locates a CSV file relative to this folder. The advantage of this method is that
the CSV file can be located no matter what folder you launch this script from.
It will also work if you click the "play" button to run the program from VS Code.
"""

import os

# this magic variable contains the path to this file
thisFilePath = __file__
print("python file path:", thisFilePath)
# python file path: .\loadFromAnywhere.py

# we can use abspath() to convert the path to an absolute path
# absolute paths start with "C:\"" on Windows, or "/" on Linux/Mac
thisFileAbsolutePath = os.path.abspath(__file__)
print("absolute python file path:", thisFileAbsolutePath)
# absolute python file path: C:\Users\scott\Documents\GitHub\Lab-Analysis\dev\csv-files\loadFromAnywhere.py

# we can use dirname() to get the path to the directory this file lives in
thisFolderPath = os.path.dirname(thisFileAbsolutePath)
print("this directory:", thisFolderPath)
# this directory: C:\Users\scott\Documents\GitHub\Lab-Analysis\dev\csv-files

# now we can locate our CSV file relative to this directory
# join() can be used to join a folder to a file path, which is
# helpful when you don't know if the folder path ends in a "/" or not
csvFilePath = os.path.join(thisFolderPath, "../../data/20817006.abf.csv")
print("CSV path:", csvFilePath)
# CSV path: C:\Users\scott\Documents\GitHub\Lab-Analysis\dev\csv-files\../../data/20817006.abf.csv

# we can use abspath() again to clean-up the file path
csvFilePath = os.path.abspath(csvFilePath)
print("CSV path absolute:", csvFilePath)
# CSV path absolute: C:\Users\scott\Documents\GitHub\Lab-Analysis\data\20817006.abf.csv

# finally we can confirm we found the file or not
if os.path.isfile(csvFilePath):
    print("CSV file found:", csvFilePath)
else:
    # this forces Python to crash with a descriptive error message
    errorMessage = "ERROR - CSV file not found: " + csvFilePath
    raise Exception(errorMessage)
