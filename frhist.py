import scipy as sp


def fr(x):
    """ 
    Freedman–Diaconis rule for selecting bin size in histograms. 
    x = array
    """
    binsize = 2*sp.stats.iqr(x)/len(x)**(1/3)
    binum = int((max(x)-min(x))/binsize)
    return binum