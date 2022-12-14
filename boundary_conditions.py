import numpy as np
from abc import abstractmethod


def get_out_of_lower_bound(qs, ps, radii, boundary):
    return np.logical_and(qs - radii < boundary[0], ps < 0)


def get_out_of_upper_bound(qs, ps, radii, boundary):
    return np.logical_and(qs + radii > boundary[1], ps > 0)


def get_out_of_bounds_particles(qs, ps, radii, boundary):
    return np.logical_or(get_out_of_upper_bound(qs, ps, radii, boundary),
                         get_out_of_lower_bound(qs, ps, radii, boundary))


class BoundaryConditionHandler():
    def __init__(self, boundaries):
        if boundaries is None:
            boundaries = [[0, 1], [0, 1]]
        self.boundaries = np.asarray(boundaries)


    def handle_boundary_conditions(self, qs, ps, radii):
        '''handle the boundary conditions'''
        n_dimensions = qs.shape[1]

        for dim in range(n_dimensions):
            qs, ps = self._handle_boundary_conditions_1d(qs, ps, dim, radii)
        return qs, ps


    @abstractmethod
    def _handle_boundary_conditions_1d(self, qs, ps, dim, radii):
        '''Handle boundary conditions in dimension dim'''


class BounceFromBoundaries(BoundaryConditionHandler):
    def __init__(self, boundaries=None):
        super().__init__(boundaries)

    def _handle_boundary_conditions_1d(self, qs, ps, d, radii):
        out_of_bounds = get_out_of_bounds_particles(qs[:, d], ps[:, d], radii, self.boundaries[d])
        ps[:, d][out_of_bounds] *= -1
        return qs, ps


class PassThroughBoundaries(BoundaryConditionHandler):
    def __init__(self, boundaries=None):
        super().__init__(boundaries)

    def _handle_boundary_conditions_1d(self, qs, ps, d, radii):
        qs[:, d] = np.where(qs[:, d] > self.boundaries[d][1], self.boundaries[d][0], qs[:, d])
        qs[:, d] = np.where(qs[:, d] < self.boundaries[d][0], self.boundaries[d][1], qs[:, d])
        return qs, ps
