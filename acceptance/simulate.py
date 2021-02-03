import numpy as np
from scipy.stats import norm
from tqdm import tqdm
from acceptance import not_pass_rate_x

def simulate_unknonwn(model:tuple, sample:tuple, sim_n=10000):
    '''
        This function will simulate the acceptance for the unknown sigma lot
        Arg:
            model: the arguments of the three model
                model_args[0]: for lambda1 of base model
                model_args[1]: for lambda2 of base model
                model_args[2]: for lambda1 of model1
                model_args[3]: for lambda2 of model1

            sample: The arguments of a group of samples
                sample_ars[0]: the numbers of a group of samples
                sample_ars[1]: for determinated variance of ditribution
                sample_arg[2]: the level of strength of samples
            sim_n: the umber of simulations
        Return: Acceptance probability corresponding to different failure rates. 
                The first row is for one condition
                The second row is for two condition
    '''
    acc_1 = []
    acc_2 = []
    n, sigma, f_cu0 = sample
    a, b, c, d = model
    for x in not_pass_rate_x:
        loc = f_cu0 - x * sigma
        rv = norm(loc=loc, scale=sigma)
        strength = rv.rvs(size=sim_n * n).reshape(sim_n, n)
        s_mean = np.mean(strength, axis=1)
        s_std = np.std(strength, axis=1)
        s_min = np.min(strength, axis=1)

        result1 = s_mean >= a * f_cu0 + b * s_std
        result2 = s_min >= c * f_cu0 + d * s_std
        result2 = np.logical_and(result1, result2)

        _acc = np.count_nonzero(result1)/sim_n        
        acc_1.append(_acc)
        _acc = np.count_nonzero(result2)/sim_n
        acc_2.append(_acc)
    return np.array([acc_1, acc_2])
    
def simulate_knonwn(model:tuple, sample:tuple, sim_n=10000):
    raise NotImplementedError
def simulate_many(combination:list, simulate_n=10000)->np.ndarray:
    '''
    This function simulate many sample and model
    Arg:
        combination: A list which element are  a tuple for the combination 
        of a model argument and a sample
    return: all result of simulation

    '''
    data = []
    for sample, model in tqdm(combination):
        n, sigma, f_cu0 = sample
        a, b, c, d, e  = model
        _data = simulate_unkonwn(model, sample, simulation_n=simulate_n)
        data.append([n, sigma, f_cu0, a, b, 0, 0] + _data[0])
        data.append([n, sigma, f_cu0, a, b, c, d] + _data[1])
        if e != None:
            data.append([n, sigma, f_cu0, a, b, e, 0] + _data[2])
    return np.array(data)