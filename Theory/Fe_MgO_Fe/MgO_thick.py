import numpy as np
import matplotlib.pyplot as plt

# electron Energy
E = np.linspace(0.01,0.99,400)

# barrier height
V0 = 1

# k
kappa = np.sqrt(V0-E)

# thickness
d = [3,4,5,6]

for thickness in d:

    T = np.exp(-2*kappa*thickness)

    plt.plot(E,T,label=f"{thickness} ML")

plt.xlabel("Energy")
plt.ylabel("Transmission")
plt.legend()

plt.grid()

plt.show()
