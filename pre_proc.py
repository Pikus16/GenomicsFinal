from pca import *
import sys
dat_dir = '../../dat/'
out_dir = 'output/'
def main():
    if len(sys.argv) <= 2:
        print("not enough command arguments")
        exit()
    dat_dir = sys.argv[1] + '/'
    out_dir = sys.argv[2] + '/'
    Y, Yt = run_pca();

if __name__ == '__main__':                                                      
    main() 
