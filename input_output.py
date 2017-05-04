import cPickle as pickle
import os

def check_dir(filename):
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc:
            print("Error in creation")
def pwrite(F, S, filename):
    check_dir(filename) 
    pickle.dump(F, open((filename + '.F.pickle'), "wb" ) )
    pickle.dump(S, open((filename + '.S.pickle'), "wb"))

def pread(filename):
    F = (pickle.load( open((filename + '.F.pickle'), "rb" ) ))
    S = (pickle.load( open((filename + '.S.pickle'), "rb" ) ))
    return F,S

def ywrite(y, yt, filename):
    check_dir(filename)
    pickle.dump(y, open((filename + '.y.pickle'), "wb" ) )
    pickle.dump(yt, open((filename + '.yt.pickle'), "wb"))

def yread(filename):
    y = (pickle.load( open((filename + '.y.pickle'), "rb" ) ))
    yt = (pickle.load( open((filename + '.yt.pickle'), "rb" ) ))
    return y,yt

def write_tiss(y, filename):
    check_dir(filename)
    pickle.dump(y, open((filename + '.y.pickle'), "wb" ) )

def read_tiss(filename):
    y = (pickle.load( open((filename + '.y.pickle'), "rb" ) ))
    return y

