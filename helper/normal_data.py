import math
import matplotlib.pyplot as plt
import numpy as np

def standard_normally_distribution(z:np.ndarray, mu=0, sigma=1): 
    '''
        This fuction will return the value normal distribution fuction.
        Arg:
            z: standard normally distribution data point
        Return:
            data_x: the data point following the N(mu, sigma)
            data_y: the density function value of the data_x

    '''
    data_x = mu + z * sigma
    data_y = np.power(z,2)
    data_y = np.exp(-data_y / 2)
    data_y = data_y /sigma / math.sqrt(2)
    
    return data_x, data_y