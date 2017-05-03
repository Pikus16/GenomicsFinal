import numpy as np
from read_data import *
from train_model import * 

def BIC_eval(Y, F, S, d = 10, h = 5):
    n = len(S)
    k = (n-1) * h
    sigma = calc_std(Y)
    mle = (1/sigma)**2 * ss_err(Y, F, S) + (np.log(2 * np.pi) * len(F) * len(S))
    return (np.log(n) * k + mle)

def centroids(Y):
    ss = 0
    for i in Y:
        for u in Y[i]:
            ss += (sum(Y[i][u])**2)
    return ss

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def plot_ss():
    bm = [f for f in os.listdir('results/basic_model/')]
    bm_files = np.sort(bm)
    Y, Yt = pca.run_pca()
    h = []
    ss_bm = []
    for g in range(0, len(bm_files), 2):
        f = (bm_files[g].split('.')[0]) 
        F, S =pread('results/basic_model/' + f)
        h.append(f.split('_')[3])
        ss_bm.append(ss_err(Y, F, S))
    h = np.asarray(h, int)
    br = [f for f in os.listdir('results/basic_randomized/')]
    br_files = np.sort(br)
    ss_br = []
    for g in range(0, len(br_files), 2):
        f = (br_files[g].split('.')[0]) 
        F, S =pread('results/basic_randomized/' + f)
        ss_br.append(ss_err(Y, F, S))
    tr = [f for f in os.listdir('results/total_randomized/')]
    tr_files = np.sort(tr)
    ss_tr = []
    for g in range(0, len(tr_files), 2):
        f = (tr_files[g].split('.')[0]) 
        F, S =pread('results/total_randomized/' + f)
        ss_tr.append(ss_err(Y, F, S))
    tm = [f for f in os.listdir('results/total_model/')]
    tm_files = np.sort(tm)
    ss_tm = []
    for g in range(0, len(tm_files), 2):
        f = (tm_files[g].split('.')[0]) 
        F, S =pread('results/total_model/' + f)
        ss_tm.append(ss_err(Y, F, S))
    plt.figure(1)
    #plt.ylim((-100,np.nanmax(np.hstack((ss_tm,ss_tr,ss_bm,ss_br)))))
    plt.scatter(h,ss_tm, color = 'red', label = 'Total Model')
    plt.scatter(h,ss_tr, color = 'blue', label = 'Total Randomized')
    plt.scatter(h,ss_bm, color = 'green', label = 'Basic Model')
    plt.scatter(h,ss_br, color = 'black', label = 'Basic Randomized')
    plt.title('SSD vs H')
    plt.xlabel('h values')
    plt.ylabel('SSD Scores')
    m = np.nanmin(np.hstack((ss_tm,ss_tr,ss_bm,ss_br)))
    plt.ylim(m * .5, m * 4.0)
    plt.xlim(0, np.nanmax(h))
    plt.legend(loc='best', shadow=False, scatterpoints=1)
    plt.savefig('SSD_Scores.png')
    plt.close(1)

def plot_bic():
    bm = [f for f in os.listdir('results/basic_model/')]
    bm_files = np.sort(bm)
    Y, Yt = pca.run_pca()
    h = []
    bic_bm = []
    for g in range(0, len(bm_files), 2):
        f = (bm_files[g].split('.')[0]) 
        F, S =pread('results/basic_model/' + f)
        h.append(f.split('_')[3])
        bic_bm.append(BIC_eval(Y, F, S))
    h = np.asarray(h, int)
    br = [f for f in os.listdir('results/basic_randomized/')]
    br_files = np.sort(br)
    bic_br = []
    for g in range(0, len(br_files), 2):
        f = (br_files[g].split('.')[0]) 
        F, S =pread('results/basic_randomized/' + f)
        bic_br.append(BIC_eval(Y, F, S))
    tr = [f for f in os.listdir('results/total_randomized/')]
    tr_files = np.sort(tr)
    bic_tr = []
    for g in range(0, len(tr_files), 2):
        f = (tr_files[g].split('.')[0]) 
        F, S =pread('results/total_randomized/' + f)
        bic_tr.append(BIC_eval(Y, F, S))
    tm = [f for f in os.listdir('results/total_model/')]
    tm_files = np.sort(tm)
    bic_tm = []
    for g in range(0, len(tm_files), 2):
        f = (tm_files[g].split('.')[0]) 
        F, S =pread('results/total_model/' + f)
        bic_tm.append(BIC_eval(Y, F, S))
    ## Plot
    plt.figure(2)
    m = np.nanmin(np.hstack((bic_tm,bic_tr,bic_bm,bic_br)))
    plt.ylim(m * .5, m * 2.0)
    plt.xlim(0, np.nanmax(h))
    plt.scatter(h,bic_tm, color = 'red', label = 'Total Model')
    plt.scatter(h,bic_tr, color = 'blue', label = 'Total Randomized')
    plt.scatter(h,bic_bm, color = 'green', label = 'Basic Model')
    plt.scatter(h,bic_br, color = 'black', label = 'Basic Randomized')
    plt.title('BIC vs H')
    plt.xlabel('h values')
    plt.ylabel('BIC Scores')
    plt.legend(loc='best', shadow=False, scatterpoints=1)
    plt.savefig('BIC_Scores.png')
    plt.close(2)

