import pytest
from acceptance.simulate import simulate
from acceptance import alpha_x

def test_simulate():
    model_arg = {"a":0.8, "b":0.8, "c":0.05, "d":0.9}
    sample_arg = {"sigma":6.0, "fcu_0":35.0, "sample_n":3}
    simulation_n = 10
    alpha = 0.95
    x = alpha_x[alpha]
    beta = simulate(model_args=model_arg
                    , sample_args=sample_arg,simulation_n=10)


