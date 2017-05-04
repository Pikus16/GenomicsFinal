import os
from pre_proc import *

## Gets all file names in data directory
def get_names():
     x = [f for f in os.listdir(dat_dir)]
     return x

from general import loadSNPs
### loads all data from data directory
def load_data():
    nams = get_names()
    data = []
    for i in nams:
        data.append(loadSNPs(dat_dir + i))
    return data

## Returns dictionary of sample names as keys and tissue names as values
#def get_samples_tiss():
    #nams = get_names()
   # dic = {}
    #for i in nams:
     #   X, samples, locs, snps = loadSNPs(dat_dir + i)
      #  for n in samples:
            
        
