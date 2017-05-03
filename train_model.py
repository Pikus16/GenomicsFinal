import numpy as np
from numpy import matmul as mx
import 'pca.py'
import 'io.py'



def train(Y, Yt, d = 10, h = 5, max_iter = 100):
    #get Y,Yt from Benny's code
    
    S = {}
    for u in Yt:
        S[u] = np.random.randn(h,1) #random normal h x 1

    #F = {}
    #for i in Y:
    #    F[i] = random normal d x h

    for ep in range(max_iter):
        nextF = solveF(Y, S)
        F = nextF

        nextS = solveS(Yt, F)
        S = nextS

    return (F,S)

def solveF(Y, S):
    F = {}
    
    for i in Y:
        Sit = []
        Yit = []
        for u in Y[i]:
            Sit.append(S[u])
            Yit.append(Y[i][u])

        Sit = np.concatenate(Sit, axis=1)
        Yit = np.concatenate(Yit, axis=1)
            
        Si = np.transpose(Sit)
        Yi = np.transpose(Yit)

        Fi = mx(mx( Yi, np.transpose(Si)), np.linalg.inv(mt(Si, np.transpose(Si)))) #needs to use matmul i believe

        F[i] = Fi

    return F

def solveS(Yt, F):
    d = F.shape[1]

    S = {}
    
    for u in Yt:
        Su = np.zeros((d,1))
        Isize = 0

        for i in Yt[u]:
            Su = Su + mx(mx(np.linalg.inv(mx(np.transpose(F[i]), F[i])), np.transpose(F[i])), Yt[u][i])
            Isize += 1

        Su = Su / Isize

        S[u] = Su

    return S
        

def randomize_data(Y, Yt):
    Z = {}
    Zt = {}
    for i in Y:
        for u in Y[i]:
            if i not in Z:
                Z[i] = {}
            if u not in Zt:
                Zt[u] = {}

            d = Y[i][u].shape[0]
            Z[i][u] = np.random.randn(d,1)
            Zt[u][i] = Z[i][u]
            
    return (Z, Zt)
            
def main():
    Y, Yt = run_pca()
    Z, Zt = randomize_data(Y, Yt)
    
    F, S = train(Y, Yt, 10, 5)
    FZ, SZ = train(Z, Zt, 10, 5)

    pwrite(F, S, 'total_model_10_5')
    pwrite(FZ, SZ, 'total_randomized_10_5')
    

if __name__ == '__main__':
    main()
