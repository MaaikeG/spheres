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


class RandomizedIntegrator(Integrator):
    def step(self, qs, ps, *args):
        qs = qs + self.dt * ps + 1e-2 * np.random.standard_normal(qs.shape)
        ps = ps + 1e-2 * np.random.standard_normal(ps.shape)
        ps.clip(-10, 10)
        return qs, ps
    