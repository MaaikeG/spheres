import numpy as np


def make_random_initial_conditions(n_particles):
    qs = np.random.uniform(0, 1, size=[n_particles, 2])
    ps = np.random.uniform(-1, 1, size=[n_particles, 2])
    radii = np.random.uniform(0, 0.001, size=[n_particles])
    return qs, ps, radii
    # c = np.random.random((n_particles)).T