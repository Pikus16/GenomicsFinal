



def train(data, d = 10, h = 5, max_iter = 100):
    #get Y,Yt from Benny's code
    
    S = {}
    for u in Yt:
        S[u] = random normal h x 1

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

        Sit = np.array(Sit)
        Yit = np.array(Yit)
            
        Si = np.transpose(Sit)
        Yi = np.transpose(Yit)

        Fi = Yi*transpose(Si)*invert(Si*transpose(Si)) #needs to use matmul i believe

        F[i] = Fi

    return F

def solveS(Yt, F):
    for u in Yt:
        Su
    
        

def main():
    #get data
    train(data, 10, 5)

if __name__ == '__main__':
    main()
