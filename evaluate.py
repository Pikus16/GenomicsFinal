import numpy as np
from read_data import *
from train_model import * 
from pre_proc import *

def BIC_eval(Y, F, S, d = 10, h = 5):
    n = len(S)
    k = (n-1) * h
    sigma = calc_std(Y)/1.2
    Pairs = 0
    for i in Y:
        for u in Y[i]:
            Pairs += 1
    mle = (1/sigma)**2 * ss_err(Y, F, S) + (np.log(2 * np.pi * sigma**2) * Pairs)
    #SSD = (float)(ss_err(Y, F, S))
    #return np.log(n)*(n-1)*h+n*(np.log(np.pi) + np.log(SSD/n)) + n
    #return np.log(n)*((n-1)*h + len(Y.keys()) * d * h) +n*(np.log(np.pi) + np.log(SSD/n)) + n 
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
    bm = [f for f in os.listdir(out_dir+'pickled/models/basic_model/')]
    bm_files = np.sort(bm)
    Y, Yt = pca.run_pca()
    Z, Zt = yread(out_dir+'pickled/tdat/random1') 
    h = []
    ss_bm = []
    for g in range(0, len(bm_files), 2):
        f = (bm_files[g].split('.')[0])
        if ( (int) (f.split('_')[3]) < 10):
            F, S =pread(out_dir+'pickled/models/basic_model/' + f)
            h.append(f.split('_')[3])
            ss_bm.append(ss_err(Y, F, S))
    h = np.asarray(h, int)
    '''br = [f for f in os.listdir('results/basic_randomized/')]
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
        ss_tr.append(ss_err(Y, F, S))'''
    br = [f for f in os.listdir(out_dir+'pickled/tdat/basic_random/')]
    br_files = np.sort(br)
    ss_br = []
    for g in range(0, len(br_files), 2):
        f = (br_files[g].split('.')[0])
        if ((int)(f.split('_')[3]) < 10):
            F, S =pread(out_dir+'pickled/tdat/basic_random/' + f)
            ss_br.append(ss_err(Z, F, S))
    tr = [f for f in os.listdir(out_dir+'pickled/tdat/total_random/')]
    tr_files = np.sort(tr)
    ss_tr = []
    for g in range(0, len(tr_files), 2):
        f = (tr_files[g].split('.')[0])
        if ((int)(f.split('_')[3]) < 10):
            F, S =pread(out_dir+'pickled/tdat/total_random/' + f)
            ss_tr.append(ss_err(Z, F, S))
    tm = [f for f in os.listdir(out_dir+'pickled/models/total_model/')]
    tm_files = np.sort(tm)
    ss_tm = []
    for g in range(0, len(tm_files), 2):
        f = (tm_files[g].split('.')[0]) 
        if ( (int) (f.split('_')[3]) < 10):
            F, S =pread(out_dir+'pickled/models/total_model/' + f)
            ss_tm.append(ss_err(Y, F, S))
            #print(f.split('_')[3] + "  " + str(ss_err(Y,F,S)))
    plt.figure(1)
    #plt.ylim((-100,np.nanmax(np.hstack((ss_tm,ss_tr,ss_bm,ss_br)))))
    plt.xlim(0, np.nanmax(h))
    plt.plot(h,ss_tm, color = 'red', label = 'Total Model')
    plt.plot(h,ss_tr, color = 'blue', label = 'Total Randomized')
    plt.plot(h,ss_bm, color = 'green', label = 'Basic Model')
    plt.plot(h,ss_br, color = 'black', label = 'Basic Randomized')
    plt.scatter(h,ss_tm, color = 'red')
    plt.scatter(h,ss_tr, color = 'blue')
    plt.scatter(h,ss_bm, color = 'green')
    plt.scatter(h,ss_br, color = 'black')
    plt.title('SSD vs H')
    plt.xlabel('h values')
    plt.ylabel('SSD Scores')
    m = np.nanmin(np.hstack((ss_tm,ss_tr,ss_bm,ss_br)))
    plt.ylim(m * .5, m * 4.0)
    plt.xlim(0, np.nanmax(h))
    plt.legend(loc='best', shadow=False, scatterpoints=1)
    plt.savefig(out_dir + 'SSD_Scores.png')
    plt.close(1)
    return ss_tm

def plot_bic():
    bm = [f for f in os.listdir(out_dir+'pickled/models/basic_model/')]
    bm_files = np.sort(bm)
    Y, Yt = pca.run_pca()
    h = []
    bic_bm = []
    for g in range(0, len(bm_files), 2):
        f = (bm_files[g].split('.')[0]) 
        if ( (int) (f.split('_')[3]) < 10):    
            F, S =pread(out_dir+'pickled/models/basic_model/' + f)
            h.append(f.split('_')[3])
            bic_bm.append(BIC_eval(Y, F, S, 10, (int) (f.split('_')[3])))
    h = np.asarray(h, int)
    '''br = [f for f in os.listdir('results/basic_randomized/')]
    br_files = np.sort(br)
    bic_br = []
    for g in range(0, len(br_files), 2):
        f = (br_files[g].split('.')[0]) 
        if ( (int) (f.split('_')[3]) < 12):
            F, S =pread('results/basic_randomized/' + f)
            bic_br.append(BIC_eval(Y, F, S))#, 10, (int) (f.split('_')[3])))
    tr = [f for f in os.listdir('results/total_randomized/')]
    tr_files = np.sort(tr)
    bic_tr = []
    for g in range(0, len(tr_files), 2):
        f = (tr_files[g].split('.')[0])
        if ( (int) (f.split('_')[3]) < 12):
            F, S =pread('results/total_randomized/' + f)
            bic_tr.append(BIC_eval(Y, F, S))#, 10, (int) (f.split('_')[3])))'''
    tm = [f for f in os.listdir(out_dir+'pickled/models/total_model/')]
    tm_files = np.sort(tm)
    bic_tm = []
    for g in range(0, len(tm_files), 2):
        f = (tm_files[g].split('.')[0]) 
        if ( (int) (f.split('_')[3]) < 10):
            F, S =pread(out_dir+'pickled/models/total_model/' + f)
            bic_tm.append(BIC_eval(Y, F, S, 10, (int) (f.split('_')[3])))
    #rand = [f for f in os.listdir('results/total_model/')]
    ## Plot
    plt.figure(2)
    #m = np.nanmin(np.hstack((bic_tm,bic_bm,bic_br, bic_tr)))
    #plt.ylim(m * .95, m * 1.05)
    plt.xlim(0, np.nanmax(h))
    plt.plot(h,bic_tm, color = 'red', label = 'Total Model') 
    #plt.plot(h,bic_tr, color = 'blue', label = 'Total Randomized')
    #plt.plot(h,bic_bm, color = 'green', label = 'Basic Model')
    #plt.plot(h,bic_br, color = 'black', label = 'Basic Randomized')
    plt.title('BIC vs H')
    plt.xlabel('h values')
    plt.ylabel('BIC Scores')
    plt.legend(loc='best', shadow=False, scatterpoints=1)
    plt.scatter(h,bic_tm, color = 'red')
    plt.savefig(out_dir + 'BIC_Scores.png')
    plt.close(2)
    return bic_tm.index(min(bic_tm))
    #return min(enumeratec(bic_tm), key=itemgetter(1))[0] 

def train_random():
    Y, Yt = yread(out_dir+'pickled/tdat/random1')
    x = range(0,10)
    for h in x:
        try:
            a = pread(out_dir+'pickled/tdat/total_random/total_model_10_' + str(h))
            b = pread(out_dir+'pickled/tdat/basic_random/basic_model_10_' + str(h))
        except:
            F, S = train(Y, Yt, 10, h)
            F_b, S_b = train_basic(Y, Yt, 10, h)

            pwrite(F, S, out_dir+'pickled/tdat/total_random/total_model_10_' + str(h))
            pwrite(F_b, S_b, out_dir+'pickled/tdat/basic_random/basic_model_10_' + str(h))

def varian(arr, j):
    return (arr[0] - arr[j])/arr[0]

def main():
    #train_random()
    j = plot_bic()
    ss = plot_ss()
    v = varian(ss, j)
    r = ('H with lowest BIC: ' + str(j))
    r += ('\nSSD for trained model on lowest BIC: ' + str(ss[j]))
    r += ('\nPercent Variance compared to centroid method: ' + str(100*v))
    print(r)
    f = open(out_dir + 'results.txt', 'wb')
    f.write(r)
    f.close()

if __name__ == '__main__':
    main()
