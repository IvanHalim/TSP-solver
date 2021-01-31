import math
import random
import numpy as np

def vectorToDistMatrix(coords):
    '''
    Create the distance matrix
    '''
    return np.linalg.norm(coords[:, np.newaxis] - coords[np.newaxis, :], axis=2)

def nearestNeighbourSolution(dist_matrix):
    '''
    Computes the initial solution (nearest neighbour strategy)
    '''
    