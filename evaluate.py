import numpy as np
from read_data import *
from train_model import * 

def BIC_eval(Y, F, S, d = 10, h = 5):
    i = Y.shape[0]
    u = Y.shape[1]
    n = d * i * u
    k = (i * d * h) + (u * h)
    X = []
    for i in Y:
        for u in Y[i]:
            for k in range(d):
                X.append(Y[i][u][k])
    sigma = np.std(X)
    mle = np.log(2) * i * u + (1/sigma)**2 * ss_err(Y, F, S)
    return (np.log(n) * k + mle)

def centroids(Y):
    ss = 0
    for i in Y:
        for u in Y[i]:
            ss += (sum(Y[i][u])**2)
    return ss
    
