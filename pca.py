from sklearn import svm, decomposition
import numpy as np
from read_data import *
from general import *

def run_pca(): 
    nams = get_names()
    tissues = {}
    all_samples = {}
    for i in nams:
        exp, samples_nam, locs, snps = loadSNPs(dat_dir + i)
        exp = np.asarray(exp)
        tissues[i] = pca_tiss(exp, samples_nam)
        for n in samples_nam:
            if (all_samples.has_key(n)):
                all_samples[n].append(i)
            else:
                all_samples[n] = [i]
    return tissues, all_samples

def pca_tiss(X, samples):
    pca = decomposition.PCA(n_components=10)
    pca.fit(X)
    dic = {}
    for j in range(0,pca.components_.shape[1]):
        dic[samples[j]] = pca.components_[:,j]
    return dic

