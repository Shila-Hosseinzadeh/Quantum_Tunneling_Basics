import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-8, 8, 1000)

# finite well
V = np.zeros_like(x)
V[(x > -2) & (x < 2)] = -5

a = [-0.2, -0.05, -0.5]

plt.figure(figsize=(8,5))

for i in range(3):
    psi = np.exp(a[i] * x**2)
    plt.plot(x, psi, label=f'ψ{i+1}, a={a[i]}')


plt.plot(x, V/5, 'k--', linewidth=2, label='Potential')

plt.xlabel('x')
plt.ylabel('Amplitude')
plt.title('Wavefunctions inside a finite well')

plt.legend()
plt.grid(True)

plt.show()
