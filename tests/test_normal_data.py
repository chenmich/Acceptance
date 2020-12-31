import pytest
import math
import numpy as np
from helper.normal_data import standard_normally_distribution

def test_standard_normally_distribution():
    fcu = 20
    sigma = 5
    mu = fcu + 1.65 * sigma 

    z = np.array([-1.65, 0])
    data_x, data_y = standard_normally_distribution(z, mu, sigma)
    
    x_criterion = mu +  z * sigma
    y_criterion = (x_criterion - mu)/sigma
    y_criterion = np.power(y_criterion, 2)
    y_criterion = np.exp(-y_criterion/2)
    y_criterion = y_criterion /math.sqrt(2)/sigma

    assert np.all(x_criterion==data_x)
    assert np.all(y_criterion==data_y)
