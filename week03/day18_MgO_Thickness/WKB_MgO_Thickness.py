"""
WKB Transmission Through MgO Barrier

Author: Shila Hosseinzadeh
Project: Quantum Tunneling Basics

Description:
This script demonstrates how the transmission probability
decreases as the MgO barrier thickness increases using
the WKB approximation.
"""

import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------
# Physical Parameters (Normalized Units)
# --------------------------------------------------

barrier_height = 1.0      # eV

energy = np.linspace(0.01, 0.99, 400)

kappa = np.sqrt(barrier_height - energy)

thicknesses = [3, 4, 5, 6]

# --------------------------------------------------
# Plot Transmission
# --------------------------------------------------

plt.figure(figsize=(8,5))

for thickness in thicknesses:

    transmission = np.exp(-2 * kappa * thickness)

    plt.plot(
        energy,
        transmission,
        linewidth=2,
        label=f"{thickness} ML"
    )

plt.xlabel("Energy (eV)", fontsize=12)

plt.ylabel("Transmission Probability", fontsize=12)

plt.title("Effect of MgO Thickness on Transmission")

plt.grid(True)

plt.legend()

plt.tight_layout()

plt.show()
