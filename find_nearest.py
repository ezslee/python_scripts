import numpy as np


def find_nearest(array, value):
    """Finds nearest value in an array and its index. Works for 1D & 2D arrays
    Doesn't work with NaN values"""
    
    if np.sum(np.isnan(array)) > 0:
        print('Remove NaN values')
    else:
        X = np.abs(array-value)
        idx = np.array(np.where(X == X.min()))
        if len(idx) > 1:
            return [array[idx[0], idx[1]], [idx[0][0], idx[1][0]]]
        else:
            return [array[idx], idx[0][0]]
        