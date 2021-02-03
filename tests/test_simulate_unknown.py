import math

import numpy as np
from scipy.stats import norm

from acceptance import not_pass_rate
from acceptance.simulate import simulate_unknonwn

import pytest

def test_simulate_unknown():   

    model1 = (1, 1.10, 1, -1.10)
    sample1 = (15, 4, 40)
    result1 = simulate_unknonwn(model1, sample1, sim_n=10000)
    n, _, _ = sample1
    _, k, _, _ = model1
    Ank = math.sqrt((1+k*k/2)/n)
    z = - norm.ppf(not_pass_rate)
    z_acc = (k - z) / Ank
    acc = 1 - norm.cdf(z_acc)
    assert np.allclose(result1[0], acc, atol=0.08)
    assert np.allclose(result1[0][1], 0.95, atol=0.02)
    assert np.allclose(result1[0][5], 0.1, atol=0.04)
    