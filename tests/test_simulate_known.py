import math

import numpy as np
from scipy.stats import norm

from acceptance import not_pass_rate
from acceptance.simulate import simulate_known

import pytest

def test_simulate_known():
    sample = (3, 4, 40)
    model = (1, 0.7, 1, -0.7)

    result = simulate_known(model, sample, sim_n=10000)
    n, _, _ = sample
    _, k, _, _ = model
    z = - norm.ppf(not_pass_rate)
    z_acc = (k - z) * math.sqrt(n)
    acc = 1 - norm.cdf(z_acc)
    assert np.allclose(result[0], acc, atol=0.02)
    assert np.allclose(result[0][8], acc[8], atol=0.01)
    assert np.allclose(result[0][1], 0.95, atol=0.01)
