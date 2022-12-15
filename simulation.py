import numpy as np
from typing import Callable


class NonInteractingParticlesSimulation():
    def __init__(self, boundary_condition_handler: Callable, integrator: Callable):
        self.handle_boundary_conditions = boundary_condition_handler
        self.integrator = integrator

    def update(self, data):
        data.qs, data.ps = self.integrator(data.qs, data.ps)
        data = self.handle_boundary_conditions(data)
        return data


    def simulate(self, data_initial):
        def generator():
            data = data_initial
            # qs = q_initial
            # ps = p_initial
            
            while True:
                data = self.update(data)
                yield data #np.c_[qs[:, 0], qs[:, 1], 1e3 * radii]
        return generator