import numpy as np
import matplotlib.pyplot as plt

k = np.linspace(-5, 5, 500)

E = k**2

plt.plot(k, E)

plt.title("Free Electron Dispersion")
plt.xlabel("Wave Vector k")
plt.ylabel("Energy")

plt.grid(True)
plt.show()