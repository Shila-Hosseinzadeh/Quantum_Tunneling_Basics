"""
Barrier Height Effect on Quantum Tunneling

Author: Shila Hosseinzadeh

Description:
Study the effect of barrier height on
electron transmission using the WKB approximation.
"""

import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------
# Physical Parameters
# -----------------------------------------

energy = np.linspace(0.01, 0.49, 400)

barrier_heights = [0.5, 1.0, 1.5, 2.0]

barrier_thickness = 4

# -----------------------------------------
# Plot
# -----------------------------------------

plt.figure(figsize=(8,5))

for barrier_height in barrier_heights:

    kappa = np.sqrt(barrier_height - energy)

    transmission = np.exp(
        -2 * kappa * barrier_thickness
    )

    plt.plot(
        energy,
        transmission,
        linewidth=2,
        label=f"{barrier_height:.1f} eV"
    )

plt.xlabel("Electron Energy (eV)")
plt.ylabel("Transmission Probability")
plt.title("Effect of Barrier Height")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
