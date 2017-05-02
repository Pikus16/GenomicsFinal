import numpy as np
import gzip


def loadSNPs(filename):
    f = open(filename, 'r')

    line = f.readline()
    line = line.strip()
    items = line.split('\t')
    sample_names = items[4:]

    X = []
    SNP_locations = []
    SNP_names = []
    for line in f:
        line = line.strip()
        items = line.split('\t')
        t = []
        for item in items[4:]:
            t.append(float(item))
        X.append(t)
        SNP_locations.append(float(items[1]))
        SNP_names.append(items[3])
        

    return (X, sample_names, SNP_locations, SNP_names)

