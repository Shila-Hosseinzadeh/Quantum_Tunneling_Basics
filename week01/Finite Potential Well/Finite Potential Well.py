import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10,10,1000)
V = np.zeros_like(x)
V[(x>-2)&(x<2)] = -3


plt.plot(x,V ,"r")
plt.xlabel ="x"
plt.ylabel = "V(x)"
plt.legend()
plt.title =("Finite Potential Well")
plt.grid()
plt.show()
