import numpy as np
from abc import abstractmethod


def get_out_of_lower_bound(qs, ps, boundary):
    return np.logical_and(qs < boundary[0], ps < 0)


def get_out_of_upper_bound(qs, ps, boundary):
    return np.logical_and(qs > boundary[1], ps > 0)


def get_out_of_bounds_particles(qs, ps, radii, boundary):
    return np.logical_or(get_out_of_upper_bound(qs, ps, boundary),
                         get_out_of_lower_bound(qs, ps, boundary))


class BoundaryConditionHandler():
    def __init__(self, boundaries):
        if boundaries is None:
            boundaries = [[0, 1], [0, 1]]
        self.boundaries = np.asarray(boundaries)


    def handle_boundary_conditions(self, data):
        '''handle the boundary conditions'''
        n_dimensions = data.qs.shape[1]

        for dim in range(n_dimensions):
            data = self._handle_boundary_conditions_1d(data, dim)
        return data


    @abstractmethod
    def _handle_boundary_conditions_1d(self, data, dim):
        '''Handle boundary conditions in dimension dim'''


class BounceFromBoundaries(BoundaryConditionHandler):
    def __init__(self, boundaries=None):
        super().__init__(boundaries)

    def _handle_boundary_conditions_1d(self, data, d):
        out_of_bounds = get_out_of_bounds_particles(data.qs[:, d], data.ps[:, d], data.radii, self.boundaries[d])
        data.ps[:, d][out_of_bounds] *= -1
        return data

