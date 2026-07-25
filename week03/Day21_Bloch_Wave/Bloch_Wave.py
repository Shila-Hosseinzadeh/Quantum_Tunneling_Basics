import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 1000)
k = 0
#k = 1
#k = 2
psi = np.exp(1j * k * x)
plt.plot(x, psi.real)
plt.title("Bloch Wave for k = 0")
plt.xlabel("Position x")
plt.ylabel("Real Part of ψ(x)")
plt.grid(True)
plt.show()

