import pytest
import numpy as np
from acceptance.simulate import simulate
from acceptance import not_pass_rate_x


def test_simulate():
    zip_model1 = (1.0, 0.95, 0.95, 0.85, 0.85)
    sample1 = (6, 25, 45)
    zip_model12 = (0.95, 1.55, 0.85, 0.85, 0.85)
    length = len(not_pass_rate_x)

    result1 = simulate(zip_model1, sample1, simulation_n=100)
    res = np.array(result1)
    assert np.all(res<=1) == True
    assert np.all(res>=0) == True
    assert res.shape == (3, length)
    
    result2 = simulate(zip_model12, sample1, simulation_n=100)
    res = np.array(result2)
    assert np.all(res<=1) == True
    assert np.all(res>=0) == True
    assert res.shape == (3, length)

    zip_model13 = (0.95, 1.55, 0.85, 0.85, None)
    result3 = simulate(zip_model13, sample1, simulation_n=100)
    res = np.array(result3)
    assert res.shape == (2, length)
    zip_model1_rate = res[0][0:1]
    assert np.all(zip_model1_rate<=1) == True
    assert np.all(zip_model1_rate>=0) == True
    