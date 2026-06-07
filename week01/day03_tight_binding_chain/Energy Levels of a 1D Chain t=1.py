import numpy as np
import matplotlib.pyplot as plt

N=10
t=1
H=np.zeros((N,N))
for i in range(N-1):
    H[i,i+1] = t
    H[i+1 ,i] = t


eigenvalues, eigenvectors = np.linalg.eigh(H)

print("Energy Levels:" , eigenvalues)

#plt.scatter(range(len(eigenvalues)), eigenvalues)
plt.plot(eigenvalues, "o-", label=f"t={t}")
plt.xlabel("State index")
plt.ylabel("Energy")
plt.title("Energy Levels of a 1D Chain")
plt.legend()
plt.show()
