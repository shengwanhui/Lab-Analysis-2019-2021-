import pandas as pd
import matplotlib.pyplot as plt

file="../../data/20817006.abf.csv"
csvData = pd.read_csv(file,sep=",",skiprows=2) # read all the data except the title and unit rows

times = csvData.iloc[:,0] # all rows from the first column

currents = csvData.iloc[:,1] # all rows from the second column
print("currents")

# plot current-over-time figure
plt.figure(figsize=(8, 4))
plt.plot(times, currents, ".-")
plt.title("Holding Current", fontsize=20)
plt.ylabel("Holding Current (pA)", fontsize=12)
plt.xlabel("Time (minutes)", fontsize=12)
plt.grid(alpha=.2, ls='--')

plt.savefig("Ihold.png")
#plt.show()

