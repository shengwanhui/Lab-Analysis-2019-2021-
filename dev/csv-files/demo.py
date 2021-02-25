import numpy as np

csvFilePath = "../../data/20817006.abf.csv"
csvData = np.loadtxt(csvFilePath, skiprows=1, delimiter=",")

times = csvData[:,0] # all rows from the first column
print(times)

currents = csvData[:,1] # all rows from the second column
print(currents)