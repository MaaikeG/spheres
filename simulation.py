import numpy as np
from typing import Callable


class NonInteractingParticlesSimulation():
    def __init__(self, boundary_condition_handler: Callable, integrator: Callable):
        self.handle_boundary_conditions = boundary_condition_handler
        self.integrator = integrator

    def update(self, qs, ps, radii):
        qs, ps = self.integrator(qs, ps)
        qs, ps = self.handle_boundary_conditions(qs, ps, radii)
        return qs, ps


    def simulate(self, q_initial, p_initial, radii):
        def generator():
            qs = q_initial
            ps = p_initial
            
            while True:
                qs, ps = self.update(qs, ps, radii)
                yield np.c_[qs[:, 0], qs[:, 1], 1e3 * radii]
        return generator