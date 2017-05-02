from sklearn import svm, decomposition
import numpy as np
from read_data import *
from general import *

def run_pca(d = 10): 
    nams = get_names()
    tissues = {}
    all_samples = {}
    for i in nams:
        exp, samples_nam, locs, snps = loadSNPs(dat_dir + i)
        exp = np.asarray(exp)
        tissues[i] = pca_tiss(exp, samples_nam, d)
      #############3
        #for n in samples_nam:
         #   if (all_samples.has_key(n)):
          #      all_samples[n].append(i)
           # else:
            #    all_samples[n] = [i]
    for n in tissues.keys():
        for j in tissues[n].keys():
            temp = {}
            temp[n] = tissues[n][j]
            if (all_samples.has_key(j)):
                all_samples[j][n] = temp.values()
            else:
                all_samples[j] = temp
    return tissues, all_samples

def pca_tiss(X, samples, d = 10):
    pca = decomposition.PCA(n_components=d)
    pca.fit(X)
    dic = {}
    for j in range(0,pca.components_.shape[1]):
        dic[samples[j]] = pca.components_[:,j]
    return dic
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def plot_tissue_pca(d = 10):
    nam_a = get_names()[0]
    nam_b = get_names()[1]
    exp_a, samples_a, locs_a, snps_a = loadSNPs(dat_dir + nam_a)
    exp_b, samples_b, locs_b, snps_b = loadSNPs(dat_dir + nam_b)
    pca = decomposition.PCA(n_components = d)
    pca.fit(exp_a)
    x = pca.components_[0,:]
    y = pca.components_[1,:]
    plt.scatter(x,y)
    
    

