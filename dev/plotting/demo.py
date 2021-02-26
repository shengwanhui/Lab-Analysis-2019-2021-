import matplotlib.pyplot as plt

currents = [3, 5, 2, 5, 6, 3, 7, 4]
times = [0, 1, 2, 3, 4, 5, 6, 7]

plt.figure(figsize=(8, 4))
plt.plot(times, currents, ".-")
plt.title("Demonstration Plot")
plt.ylabel("Holding Current (pA)")
plt.xlabel("Time (minutes)")
plt.grid(alpha=.2, ls='--')

plt.savefig("demo.png")
#plt.show()