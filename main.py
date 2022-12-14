import numpy as np
from animate import AnimatedScatter
import matplotlib.pyplot as plt
from simulation import NonInteractingParticlesSimulation
from boundary_conditions import BounceFromBoundaries, PassThroughBoundaries
from integrator import SimpleIntegrator, RandomizedIntegrator

n_particles = 10
boundaries = np.asarray([[0, 1], [0, 1]])

if __name__ == '__main__':
    qs = np.random.uniform(0, 1, size=[n_particles, 2])
    ps = np.random.uniform(-1, 1, size=[n_particles, 2])
    radii = np.random.uniform(0, 0.001, size=[n_particles])

    boundary_handler = BounceFromBoundaries().handle_boundary_conditions
    intergrator = RandomizedIntegrator(dt=0.005).step
    simulation = NonInteractingParticlesSimulation(
        boundary_condition_handler=boundary_handler, 
        integrator=intergrator)


    def data_generator():
        """Generate a random walk (brownian motion). Data is scaled to produce
        a soft "flickering" effect."""
        qs = np.random.uniform(0, 1, size=[n_particles, 2])
        ps = np.random.uniform(-1, 1, size=[n_particles, 2])
        radii = np.random.uniform(0, 0.001, size=[n_particles])

        c = np.random.random((n_particles)).T
        while True:
            qs, ps = simulation.update(qs, ps, radii)
            yield np.c_[qs[:, 0], qs[:, 1], 1e3 * radii, c]


    a = AnimatedScatter(data_generator, ax_limits=boundaries.reshape(-1))
    plt.show()
