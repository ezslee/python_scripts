import numpy as np


def bootstrap(array, iterations, bound):
    """
    Calculates non-parametric, empirical bootstrap confidence intervals
    for 'n' iterations. Parameter 'bound' is confidence bound in decimal
    format. 'Iterations' are number of bootstrap samples to calculate
    """
    initial = np.empty(shape=(array.size, iterations), dtype=float)
    for step in np.arange(0, iterations, 1):
        resample = np.random.choice(array, array.size, replace=True)
        initial[:, step] = resample
    samplemean = np.mean(array)
    bootstrapmean = np.mean(initial, axis=0)
    stackedmean = np.sort(bootstrapmean-samplemean)
    upperboundpercent = 1-(1-bound)/2
    lowerboundpercent = (1-bound)/2
    upperboundval = stackedmean[round(upperboundpercent*(stackedmean.size-1))]
    lowerboundval = stackedmean[round(lowerboundpercent*(stackedmean.size-1))]
    upperrange = samplemean - lowerboundval
    lowerrange = samplemean - upperboundval
    return [bootstrapmean, upperrange, lowerrange]