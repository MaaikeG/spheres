import numpy as np
from abc import abstractmethod


class Integrator():
    def __init__(self, dt=1e-3):
        self.dt = dt

    @abstractmethod
    def step(qs, ps, *args):
        '''Do a step'''


class SimpleIntegrator(Integrator):
    def step(self, qs, ps, *args):
        return qs + self.dt * ps, ps
