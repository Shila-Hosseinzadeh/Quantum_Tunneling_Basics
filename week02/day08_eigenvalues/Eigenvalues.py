import numpy as np

N = 5

H = np.zeros((N,N))

for i in range(N-1):
    H[i,i+1] = -1
    H[i+1,i] = -1
eigenvalues, eigenvectors = np.linalg.eigh(H)

print("Eigenvalues:")
print(eigenvalues)
