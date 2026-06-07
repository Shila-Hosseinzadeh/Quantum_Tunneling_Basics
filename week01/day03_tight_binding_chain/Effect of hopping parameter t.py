import numpy as np
import matplotlib.pyplot as plt

N = 10

t_values = [-0.5, -1, -2]

plt.figure(figsize=(8,5))

for t in t_values:
    H = np.zeros((N, N))

    for i in range(N-1):
        H[i, i+1] = t
        H[i+1, i] = t

    eigenvalues, _ = np.linalg.eigh(H)

    plt.plot(eigenvalues, 'o-', label=f't = {t}')

plt.xlabel("State index")
plt.ylabel("Energy")
plt.title("Effect of hopping parameter t")
plt.legend()
plt.show()
