import matplotlib.pyplot as plt

plt.scatter(range(len(eigenvalues)), eigenvalues)

plt.xlabel("State Index")
plt.ylabel("Energy")
plt.title("Energy Spectrum")

plt.grid(True)

plt.show()
