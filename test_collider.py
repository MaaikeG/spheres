import simulation
import numpy as np

def test_out_of_lower_bound():
    boundary = 1.

    qs = np.asarray([0., 1., 2.])
    radii = np.asarray([0., 1., 1.]) 

    get_out_of_lower_bound(qs, radii, boundary)