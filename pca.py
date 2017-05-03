
from sklearn import decomposition
import numpy as np
from read_data import *
from general import *
import os
from input_output import *

def run_pca(d = 10): 
    try:
        y, yt = yread(tiss_nam)
        return y, yt
    except:
        #nams = get_names()
        #tissues = {}
        tissues = get_tissues(d)
        Y = tissues

        Yt = {}
        for i in Y:
            for u in Y[i]:
                if u not in Yt:
                    Yt[u] = {}

                Yt[u][i] = Y[i][u]
        
        ywrite(Y, Yt, tiss_nam)
        return Y, Yt

tiss_nam = 'dat'
def pca_tiss(X, samples, d = 10):
    pca = decomposition.PCA(n_components=d)
    pca.fit(X)
    dic = {}
    for j in range(0,pca.components_.shape[1]):
        dic[samples[j]] = np.reshape(pca.components_[:,j],(d,1)) 
    return dic

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def get_tissues(d= 10):
    try:
        tissues = read_tiss(tiss_nam)
        return tissues
    except:
        nams = get_names()
        tissues = {}
        all_samples = {}
        for i in nams:
            exp, samples_nam, locs, snps = loadSNPs(dat_dir + i)
            exp = np.asarray(exp)
            tissues[i] = pca_tiss(exp, samples_nam, d)
        write_tiss(tissues, tiss_nam)
        return tissues

def plot_tissue_pca(d = 10):
    tissues = get_tissues(d)
    s = 32
    first = tissues[tissues.keys()[s]]
    x = 0.
    y = 0.
    for j in first.keys():
        x += first[j][0]
        y += first[j][1]
    x /= len(first.keys())
    y /= len(first.keys())
    plt.figure(s)
    red = []
    blue = []
    purple = []
    green = []
    for n in first.keys():
        if (first[n][0] >= x):
            if (first[n][1] >= y):
                plt.scatter(first[n][0], first[n][1], color = 'red')
                red.append(n)
            else:
                plt.scatter(first[n][0], first[n][1], color = 'blue')
                blue.append(n)
        else:
            if (first[n][1] >= y):
                plt.scatter(first[n][0], first[n][1], color = 'purple')
                purple.append(n)
            else:
                plt.scatter(first[n][0], first[n][1], color = 'green')
                green.append(n)
    plt.title(str(tissues.keys()[s]))
    plt.savefig(str(tissues.keys()[s]) + '.png')
    plt.close(s)
    for i in range(0, 33):
        if (i != s):
            plt.figure(i)
            dims = tissues[tissues.keys()[i]]
            for n in dims.keys():
                if (n in red):
                    plt.scatter(dims[n][0], dims[n][1], color = 'red')
                elif (n in blue):
                    plt.scatter(dims[n][0], dims[n][1], color = 'blue')
                elif (n in purple):
                    plt.scatter(dims[n][0], dims[n][1], color = 'purple')
                elif (n in green):
                    plt.scatter(dims[n][0], dims[n][1], color = 'green')
                else:
                    plt.scatter(dims[n][0], dims[n][1], color = 'black')
            plt.title(str(tissues.keys()[i]))
            plt.savefig(str(tissues.keys()[i]) + '.png')
            plt.close(i)
    return 
    
    

