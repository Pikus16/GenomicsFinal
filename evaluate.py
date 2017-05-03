import numpy as np
def BIC_eval(Y, F, S, d = 10, h = 5):
    i = Y.shape[0]
    u = Y.shape[1]
    n = d * i * u
    k = (i * d * h) + (u * h)
    mle = np.log(2) * i * u
    return (np.log(n) * k + mle)
