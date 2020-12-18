import numpy as np

def simulate(model_args:map, sample_args:map, simulation_n=10000):
    raise NotImplementedError
    x_alpha = sample_args['x_alpha']
    sigma = sample_args['sigma']
    sample_n = sample_args['sample_n']
    fcu_0 = sample_args['fcu_0']
    fcu = fcu_0 + x_alpha * sigma

    simulate_data = np.random \
                        .standard_normal(sample_n * simulation_n) \
                        .reshape(simulation_n, sample_n)
    simulate_data += fcu + simulate * sigma
    
