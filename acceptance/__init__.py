import collections
import itertools
import numpy as np
from scipy.stats  import norm

not_pass_rate = [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50, 0.60, 0.70, 0.75, 0.85, 0.95]
not_pass_rate_x = norm.ppf(not_pass_rate)

def get_sample_model():
    '''
    This function return all the combination of samples and models
    return：
        a list which element is consist of a sample and a model
    '''
    #argments for sample
    __sample_num = [12, 14, 18, 22, 30, 50]
    __f_cu0 = [20, 25, 30, 35, 40, 45, 50]
    __sigma = [2.5, 3.0, 4.0, 5.0, 6.0, 8.0, 10.0]
    #samples
    samples = [(x, y) for x in __sample_num for y in __sigma]
    samples = [(x, y , z) for x, y in samples for z in __f_cu0]

    #argments for model
    a = np.arange(0.80, 1.2, 0.05)
    b = np.arange(0.80, 1.80, 0.05)
    c = np.arange(0.80, 1.20, 0.05)
    d = np.arange(0.80, 1.20, 0.05)
    e = np.arange(0.80, 1.15, 0.05)
    #model
    __mode1_arg = [(x, y) for x in a for y in b]
    __model2_arg = [(x, y) for x in c for y in d]
    __combined_arg = itertools.zip_longest(__model2_arg, e, fillvalue=None)
    __com = [(x[0][0], x[0][1], x[1]) for x in __combined_arg]
    models = [(a, b, c, d, e) for a, b in __mode1_arg 
                                for c, d, e in __com]
    combination = [(sample, model) for sample in samples for model in models]
    return combination