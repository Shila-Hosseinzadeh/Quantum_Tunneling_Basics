import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-10,10,1000)
psi_1=np.exp(-x**2)
psi_2=np.exp(-2*x**2)
psi_3=np.exp(-0.5*x**2)

plt.plot(x,psi_1 , label =r'$\psi_1(x)$' )
plt.plot(x,psi_2 , label = r'$\psi_2(x)$')
plt.plot(x,psi_3 , label = r'$\psi_3(x)$')
plt.xlabel("x")
plt.ylabel(r'$\psi(x)$')
plt.legend()
plt.show()
