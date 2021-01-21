import pytest
import numpy as np
from acceptance.simulate import simulate_many

def test_simulate_many():
    combination =[
        ((12, 2.5, 20),(1.15, 1.6, 0.9, 0.8, 0.85)),
        ((18, 3.5, 45),(1.10, 1.65, 0.85, 0.7, None))
    ]
    result = simulate_many(combination, simulate_n=10)

    assert len(result) == 5
    assert np.all(result[0][0:7]==
                    [12, 2.5, 20, 1.15, 1.6, 0, 0]) == True
    assert np.all(result[1][0:7]==
                    [12, 2.5, 20, 1.15, 1.6, 0.9, 0.80])==True
    assert np.all(result[2][0:7]==
                    [12, 2.5, 20, 1.15, 1.6, 0.85, 0])==True
    assert np.all(result[3][0:7]==
                    [18, 3.5, 45, 1.10, 1.65, 0, 0])==True
    assert np.all(result[4][0:7]==
                    [18, 3.5, 45, 1.10, 1.65, 0.85, 0.7])==True