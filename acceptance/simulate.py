import numpy as np
from collections import OrderedDict
from acceptance import alpha_x

def simulate(model_args:tuple, sample_args:tuple, simulation_n=10000):
    #model
    a = model_args[0]
    b = model_args[1]
    c = model_args[2]
    d = model_args[3]
    e = model_args[4]
    #sample
    sigma = sample_args[0]
    n = sample_args[1]
    f_cu0 = sample_args[2]
    
    beta = []
    beta1 = []
    beta2 = []
    for _, x in alpha_x.items():
        data = np.random.normal(size=n * simulation_n).reshape(simulation_n, n)
        m_f = f_cu0 - x * sigma
        data = m_f + sigma * data
        s_mean = np.mean(data, axis=1)
        std = np.std(data, axis=1)
        s_min = np.min(data, axis=1)
        base = s_mean - (a * f_cu0 + b * std)
        model1 = s_min - (c * f_cu0 - d * std)

        base_result = base >= 0
        model1_result = model1 >= 0

        base_rate = np.count_nonzero(base_result) / simulation_n
        zip_model1_rate = np.count_nonzero( \
                    np.logical_and(model1_result, base_result)) / simulation_n
        if e is None:
            zip_model2_rate = None
        else:
            model2 = s_min - e * f_cu0
            model2_reuslt = model2 >= 0
            zip_model2_rate = np.count_nonzero(\
                        np.logical_and(base_result, model2_reuslt)) / simulation_n
        beta.append(base_rate)
        beta1.append(zip_model1_rate)
        beta2.append(zip_model2_rate) 
    beta = [beta, beta1, beta2]
    return beta
        
