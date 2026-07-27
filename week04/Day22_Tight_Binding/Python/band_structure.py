"""
=========================================================
Day 22 - Tight Binding Band Structure
Course: Quantum Transport
Author: Shila Hosseinzadeh
=========================================================

This program plots the energy band of a 1D Tight-Binding model.

Equation:
    E(k) = E0 - 2*t*cos(k*a)

"""

# ======================================================
# Import Libraries
# ======================================================

import numpy as np
import matplotlib.pyplot as plt

# ======================================================
# Physical Parameters
# ======================================================

t = 1.0          # Hopping parameter (eV)

E0 = 0.0         # Atomic energy (eV)

a = 1.0          # Lattice constant

# ======================================================
# k-space
# First Brillouin Zone
# ======================================================

k = np.linspace(-np.pi/a, np.pi/a, 500)

# ======================================================
# Tight-Binding Energy
# ======================================================

E = E0 - 2*t*np.cos(k*a)

# ======================================================
# Plot
# ======================================================

plt.figure(figsize=(8,6))

plt.plot(k, E,
         color='blue',
         linewidth=2,
         label='Tight-Binding Band')

plt.xlabel("Wave Vector k", fontsize=12)

plt.ylabel("Energy (eV)", fontsize=12)

plt.title("1D Tight-Binding Band Structure", fontsize=14)

plt.grid(True)

plt.legend()

plt.tight_layout()

# ======================================================
# Save Figure
# ======================================================

plt.savefig("../Figures/band_structure.png", dpi=300)

# ======================================================
# Show Figure
# ======================================================

plt.show()