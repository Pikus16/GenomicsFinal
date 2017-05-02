import numpy as np
import random
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

def split_test(infile, trainfile, testfile):
    fin = open(infile, 'r')

    ftrain = open(trainfile, 'w')
    ftest = open(testfile, 'w')

    portion = 0.1


    header = fin.readline()
    ftrain.write(header)
    ftest.write(header)


    for line in fin:
        r = random.random()

        if r < portion:
            ftest.write(line)
        else:
            ftrain.write(line)
