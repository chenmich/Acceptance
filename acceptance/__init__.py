import collections
import itertools
import numpy as np
from scipy.stats  import norm

not_pass_rate = np.array([0.01, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50, 
                            0.60, 0.70, 0.75, 0.85, 0.95])
not_pass_rate_x = norm.ppf(not_pass_rate)
def get_sample_model_unknown():
    '''
    This function return all the combination of samples and models for unknown sigma
    return：
        a list which element is a tuple of a sample and a model
    '''
    #argments for sample
    __sample_num = [10, 15, 20, 30, 50]
    __f_cu0 = [20, 30, 40, 50, 60]
    __sigma = [2.5, 4.5, 5.5, 8.0, 12.0]
    #samples
    samples = [(x, y) for x in __sample_num for y in __sigma]
    samples = [(x, y , z) for x, y in samples for z in __f_cu0]

    #argments for model
    a = np.arange(0.85, 1.20, 0.05)
    b = np.arange(0.85, 1.80, 0.05)
    c = np.arange(0.85, 1.20, 0.05)
    d = np.arange(0.85, 1.20, 0.05)
    
    #model
    __mode1_arg = [(x, y) for x in a for y in b]
    __model2_arg = [(x, y) for x in c for y in d]
    models = [(a, b, c, d) for a, b in __mode1_arg for c, d in __model2_arg]

    combination = [(sample, model) for sample in samples for model in models]
    return combination

def get_sample_model_known():
    '''
    This function return all the combination of samples and models for known sigma
    return：
        a list which element is a tuple of a sample and a model
    '''

    #argments for sample
    __sample_num = [3, 4, 5, 6, 8, 10, 15, 20]
    __f_cu0 = [20, 30, 40, 50, 60]
    __sigma = [2.5, 4.5, 5.5, 8.0, 12.0]
    #samples
    samples = [(x, y) for x in __sample_num for y in __sigma]
    samples = [(x, y , z) for x, y in samples for z in __f_cu0]

    #argments for model
    a = np.arange(0.85, 1.20, 0.05)
    b = np.arange(0.55, 0.90, 0.05)
    c = np.arange(0.80, 1.20, 0.05)
    d = np.arange(-0.85, -0.50, 0.05)
    
    #model
    __mode1_arg = [(x, y) for x in a for y in b]
    __model2_arg = [(x, y) for x in c for y in d]
    models = [(a, b, c, d) for a, b in __mode1_arg for c, d in __model2_arg]

    com = [(sample, model) for sample in samples for model in models]
    return com