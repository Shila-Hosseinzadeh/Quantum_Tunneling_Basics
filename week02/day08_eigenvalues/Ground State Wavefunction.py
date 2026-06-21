import numpy as np

N = 5

H = np.zeros((N,N))

for i in range(N-1):
    H[i,i+1] = -1
    H[i+1,i] = -1
plt.plot(ground_state, marker='o')

plt.title("Ground State Wavefunction")
plt.xlabel("Site")
plt.ylabel("Amplitude")

plt.grid(True)

plt.show()
