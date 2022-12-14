from typing import Callable


class NonInteractingParticlesSimulation():
    def __init__(self,  boundary_condition_handler: Callable, integrator: Callable):
        self.handle_boundary_conditions = boundary_condition_handler
        self.integrator = integrator

    def update(self, qs, ps, radii):
        qs, ps = self.integrator(qs, ps)
        qs, ps = self.handle_boundary_conditions(qs, ps, radii)
        return qs, ps
