import os

dat_dir = '../../dat/'
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
