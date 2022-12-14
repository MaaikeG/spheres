import numpy as np
from animate import AnimatedScatter
import matplotlib.pyplot as plt
from simulation import NonInteractingParticlesSimulation
from boundary_conditions import BounceFromBoundaries, PassThroughBoundaries
from integrator import SimpleIntegrator, RandomizedIntegrator
import initial_conditions


n_particles = 10
boundaries = np.asarray([[0, 1], [0, 1]])


if __name__ == '__main__':
    qs, ps, radii = initial_conditions.make_random_initial_conditions(n_particles)

    boundary_handler = BounceFromBoundaries().handle_boundary_conditions
    intergrator = RandomizedIntegrator(dt=0.005).step
    simulation = NonInteractingParticlesSimulation(
        boundary_condition_handler=boundary_handler, 
        integrator=intergrator)

    a = AnimatedScatter(simulation.simulate(qs, ps, radii), ax_limits=boundaries.reshape(-1))
    plt.show()
