import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 1000)

# barrier
V = np.zeros_like(x)
V[(x > -1) & (x < 1)] = 5

# fake tunneling wave intuition
psi = np.exp(-0.1*(x+3)**2)

# weaken inside barrier
psi[(x > -1) & (x < 1)] *= 0.3

 # change psi[ (x > -3) & (x < 3)] *= 0.3

# small transmitted wave
psi[x > 1] *= 0.2

plt.figure(figsize=(8,5))

plt.plot(x, psi, label='Wavefunction')
plt.plot(x, V/5, 'k--', label='Barrier')

plt.xlabel('x')
plt.ylabel('Amplitude')
plt.title('Quantum Tunneling Intuition')
plt.legend()
plt.grid(True)

plt.show()
