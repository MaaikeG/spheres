import numpy as np
from animate import AnimatedScatter
import matplotlib.pyplot as plt
from collider import NonInteractingParticlesSimulation

n_particles = 10
boundaries = np.asarray([[0, 1], [0, 1]])

if __name__ == '__main__':
    qs = np.random.uniform(0, 1, size=[n_particles, 2])
    ps = np.random.uniform(-1, 1, size=[n_particles, 2])
    radii = np.random.uniform(0, 0.001, size=[n_particles])

    simulation = NonInteractingParticlesSimulation(qs, ps, radii, dt=0.005)


    def data_generator():
        """Generate a random walk (brownian motion). Data is scaled to produce
        a soft "flickering" effect."""
        c = np.random.random((n_particles)).T
        while True:
            simulation.update()
            yield np.c_[simulation.qs[:, 0], simulation.qs[:, 1], 1e3 * simulation.radii, c]


    a = AnimatedScatter(data_generator, ax_limits=boundaries.reshape(-1))
    plt.show()
