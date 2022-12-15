from abc import abstractmethod
import numpy as np


class Integrator():
    def __init__(self, dt=1e-3):
        self.dt = dt

    @abstractmethod
    def step(self, qs, ps, *args):
        '''Do a step'''


class SimpleIntegrator(Integrator):
    def step(self, qs, ps, *args):
        return qs + self.dt * ps, ps


class NewIntegrator(Integrator):
    def step(self, qs, ps, *args):
        return qs, np.zeros_like(qs)

class RandomizedIntegrator(Integrator):
    def step(self, qs, ps, *args):
        qs = qs + self.dt * ps + 1e-2 * np.random.standard_normal(qs.shape)
        ps = ps + 1e-2 * np.random.standard_normal(ps.shape)
        ps.clip(-10, 10)
        return qs, ps
    