import numpy as np
from collections import OrderedDict
from acceptance import alpha_x

def simulate(model_args:tuple, sample_args:tuple, simulation_n=10000):
    '''
        This function will simulate the acceptance with a group of sample
        by all the model.
        Arg:
            model_args: the arguments of the three model
                model_args[0]: for lambda1 of base model
                model_args[1]: for lambda2 of base model
                model_args[2]: for lambda1 of model1
                model_args[3]: for lambda2 of model1
                model_args[4]: for lambda2 of model2
            sample_args: The arguments of a group of samples
                sample_ars[0]: for determinated variance of ditribution
                sample_ars[1]: the numbers of a group of samples
                sample_arg[2]: the level of strength of samples  
    '''
    #model
    a, b, c, d, e = model_args
    #sample
    sigma, n, f_cu0 = sample_args
    
    beta = []
    beta1 = []
    beta2 = []
    for _, x in alpha_x.items():
        #generate data
        data = np.random.normal(size=n * simulation_n).reshape(simulation_n, n)
        m_f = f_cu0 - x * sigma
        data = m_f + sigma * data
        #compute the mean, std and min
        s_mean = np.mean(data, axis=1)
        std = np.std(data, axis=1)
        s_min = np.min(data, axis=1)
        
        #accept by base and mode1 respectively
        base = s_mean - (a * f_cu0 + b * std)
        model1 = s_min - (c * f_cu0 - d * std)
        base_result = base >= 0
        model1_result = model1 >= 0

        #compute the base's rate
        base_rate = np.count_nonzero(base_result) / simulation_n
        #compute the rate of base and model1
        zip_model1_rate = np.count_nonzero( \
                    np.logical_and(model1_result, base_result)) / simulation_n
        
        #compute the rate of base and model2
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
    if np.all(np.array([beta2])==None):
        beta = [beta, beta1]
    else:
        beta = [beta, beta1, beta2]
    return beta
        
