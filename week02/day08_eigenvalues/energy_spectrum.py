import matplotlib.pyplot as plt
import numpy as np

N = 5

H = np.zeros((N,N))

for i in range(N-1):
    H[i,i+1] = -1
    H[i+1,i] = -1

plt.scatter(range(len(eigenvalues)), eigenvalues)

plt.xlabel("State Index")
plt.ylabel("Energy")
plt.title("Energy Spectrum")

plt.grid(True)

plt.show()
