import numpy as np
from scipy.stats import maxwell

N = 50_000

kicks = maxwell(scale=265).rvs(N)
phi = np.random.uniform(0, 2*np.pi, N)
theta = np.arccos(1 - 2 * np.random.rand(N)) - np.pi / 2

with open('compas_grid.txt', 'w') as f:
    for i in range(N):
        labels = ["initial-mass-1", "initial-mass-2", "eccentricity", "orbital-period", "metallicity", "kick-magnitude-distribution", "remnant-mass-prescription", "kick-magnitude-1", "kick-theta-1", "kick-phi-1"]
        vals = [20.0, 15.0, 0.0, 100.0, 0.02, "MAXWELLIAN", "FRYER2012", kicks[i], theta[i], phi[i]]
        f.write('  '.join(f'--{label} {val}' for label, val in zip(labels, vals)) + "\n")
