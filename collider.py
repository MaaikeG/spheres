import numpy as np


def get_out_of_lower_bound(qs, ps, radii, boundary):
    return np.logical_and(qs - radii < boundary[0], ps < 0)


def get_out_of_upper_bound(qs, ps, radii, boundary):
    return np.logical_and(qs + radii > boundary[1], ps > 0)


def get_out_of_bounds_particles(qs, ps, radii, boundary):
    return np.logical_or(get_out_of_upper_bound(qs, ps, radii, boundary),
                         get_out_of_lower_bound(qs, ps, radii, boundary))


class NonInteractingParticlesSimulation():

    def __init__(self, qs, ps, radii, dt=0.1, boundaries=[[0, 1], [0, 1]]):
        self.boundaries = boundaries

        self.qs = qs
        self.ps = ps
        self.dt = dt
        self.radii = radii


    def update(self):
        self.compute_new_positions()
        self.compute_new_momenta()
        return self.qs


    def compute_new_positions(self):
        self.qs = self.qs + self.dt * self.ps


    def compute_new_momenta(self):
        n_dimensions = self.qs.shape[1]

        for d in range(n_dimensions):
            out_of_bounds = get_out_of_bounds_particles(self.qs[:, d], self.ps[:, d], self.radii, self.boundaries[d])
            self._invert_velocities(d, out_of_bounds)


    def _invert_velocities(self, d, out_of_bounds):
        new_ps = self.ps[:, d][out_of_bounds] * -1
        np.place(arr=self.ps[:, d], mask=out_of_bounds, vals=new_ps)
