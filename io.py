import cPickle as pickle

def pwrite(F, S, filename):
    pickle.dump(F, open((filename + '.F.pickle'), "wb" ) )
    pickle.dump(S, open((filename + '.S.pickle'), "wb"))

def pread(filename):
    F = (pickle.load( open((filename + '.F.pickle'), "rb" ) ))
    S = (pickle.load( open((filename + '.S.pickle'), "rb" ) ))
    return F,S
