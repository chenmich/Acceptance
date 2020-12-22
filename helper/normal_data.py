import math
import matplotlib.pyplot as plt
import numpy as np

def normal_data(mu=0, sigma=1): 
    '''
        This fuction will return a pair 
        of normal distribution fuction value.
        Arg:
            mu:    the mean of 
            sigma: the variance of distribution
        Return:
            data_x : independent variable‘s value
            data_y : dependent variable's value

    '''
    data_x = np.arange(mu - 3 * sigma, 
                mu + 3 * sigma, step=0.2)#generate the x
    data_y = data_x - mu   
    data_y = np.power(data_y, 2)
    data_y = data_y / (-2 * sigma * sigma)
    data_y = np.exp(data_y)
    data_y = data_y / math.sqrt(2 * 3.1415)
    data_y = data_y /sigma
    return data_x, data_y