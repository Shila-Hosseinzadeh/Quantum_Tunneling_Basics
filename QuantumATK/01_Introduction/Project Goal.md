# QuantumATK for Magnetic Tunnel Junctions

## Project Goal

This project is a step-by-step study of atomic-scale quantum transport using QuantumATK 2016.4.

The main research direction is quantum tunneling in nanoscale magnetic devices, with a focus on magnetic tunnel junctions and magnetic/spin diode structures.

The main model system used for learning is:

$$
\mathrm{Fe/MgO/Fe}
$$

The transport calculations will be developed using DFT and NEGF methods.

## Learning Path

The workflow is developed in the following order:

1. QuantumATK environment and project management
2. Bulk Fe
3. Bulk MgO
4. DFT and calculator parameters
5. Geometry optimization
6. Fe/MgO/Fe magnetic tunnel junction
7. Electrode and central-region construction
8. NEGF device calculations
9. Transmission spectrum
10. Spin-dependent transport
11. Parallel and antiparallel configurations
12. Current-voltage characteristics
13. Tunnel magnetoresistance
14. Convergence tests
15. Magnetic tunnel diode structures
16. Rectification and spin-dependent diode behavior

## Main Principle

For every simulation parameter, the following questions should be answered:

* What does the parameter mean?
* What physical quantity does it affect?
* Which value is used?
* Why is this value selected?
* How sensitive are the results to this parameter?
* When should the parameter be changed?

## First Calculation

The first calculation is a spin-polarized DFT calculation of bulk Fe.

The purpose is to verify that the structure, exchange-correlation functional, basis set, k-point sampling, spin polarization, and SCF convergence are working correctly before constructing the Fe/MgO/Fe device.

## Software

* QuantumATK 2016.4
* QuantumATK Python scripting
* Python
* MATLAB for numerical analysis and post-processing

## Reference Workflow

The official QuantumATK Fe/MgO/Fe spin-transport tutorial is used as one of the main references for the transport workflow.
