import numpy as np

def calculate(l):
    '''
        Reshapes the input list of 9 elements to a 3x3 array and returns a dictionary
        containing mean, variance, standard deviation, max, min elements and the sum
        along the axis and of the flattened list.
        Throws exception in if the input list is not 9 elements long.
    '''
    if len(l)!=9:
          raise ValueError("List must contain nine numbers.")
    l = np.reshape(l, (3,3))
    calculations = {
    'mean': [list(np.mean(l, axis=0)), list(np.mean(l, axis=1)), np.mean(l)],
    'variance': [list(np.var(l, axis=0)), list(np.var(l, axis=1)), np.var(l)],
    'standard deviation': [list(np.nanstd(l, axis=0)), list(np.nanstd(l, axis=1)), np.nanstd(l)],
    'max': [list(np.amax(l, axis=0)), list(np.amax(l, axis=1)), np.amax(l)],
    'min': [list(np.amin(l, axis=0)), list(np.amin(l, axis=1)), np.amin(l)],
    'sum': [list(np.sum(l, axis=0)), list(np.sum(l, axis=1)), np.sum(l)]

  }


    return calculations