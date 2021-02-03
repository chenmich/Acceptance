import pytest
import numpy as np
from acceptance.simulate import simulate_many, simulate_known

def test_simulate_many():
    combination =[
        ((12, 2.5, 20),(1.0, 1.15, 0.9, 0.0)),
        ((18, 3.5, 45),(1.0, 1.10, 0.9, 0.0))
    ]
    result = simulate_many(combination, sim_n=10)

    assert np.all(result[0][0:7]==
                    [12, 2.5, 20, 1.0, 1.15, 0.0, 0]) == True
    assert np.all(result[1][0:7]==
                    [12, 2.5, 20, 1.0, 1.15, 0.9, 0])==True
    assert np.all(result[2][0:7]==
                    [18, 3.5, 45, 1.0, 1.10, 0.0, 0])==True
    assert np.all(result[3][0:7]==
                    [18, 3.5, 45, 1.0, 1.10, 0.9, 0])==True
    
    combination =[
        ((3, 2.5, 20),(1.0, 0.70, 1.0, -0.70)),
        ((4, 3.5, 45),(1.0, 0.65, 1.0, -0.65))
    ]
    result = simulate_many(combination, sim_fuc=simulate_known, sim_n=10000)
    assert np.all(result[0][0:7]==
                    [3, 2.5, 20, 1.0, 0.70, 0.0, 0.00]) == True
    assert np.all(result[1][0:7]==
                    [3, 2.5, 20, 1.0, 0.70, 1.0, -0.70])==True
    assert np.all(result[2][0:7]==
                    [4, 3.5, 45, 1.0, 0.65, 0.0, 0.00])==True
    assert np.all(result[3][0:7]==
                    [4, 3.5, 45, 1.0, 0.65, 1.0, -0.65])==True