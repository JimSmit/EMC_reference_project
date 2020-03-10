# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 12:36:54 2020

@author: 31643
"""

# Import libraries
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import os
import EMC_library


# set home directory
os.getcwd()
os.chdir('C:\\Users\\31643\\Documents\\REF_PROJECT_EMC')


# Clean data
data = EMC_library.data_cleaner('ref_data_emc_200304.csv',n=10000)

# Count dataset tests
count_df_department = EMC_library.counter(data)    # create amount of tests per department







# Top departments 

totals_per_department = count_df_department.sum(axis=0)
totals_per_department = totals_per_department.sort_values()

top_30_departments = totals_per_department.nlargest(n=30)

# Top keys
totals_per_key = count_df_keys.sum(axis=0)
totals_per_key = totals_per_key.sort_values()

top_30_keys = totals_per_key.nlargest(n=30)







# variance of different keys

def data_spreadings(dataset):
    import statistics
    # Number of samples
    n_samples = dataset.shape[0]
    
    keys = dataset.CODE_BEPALING.unique()

    biglist = []
    count = 0
    for key in keys:
        lst = list()
        for i in range(n_samples):
            if dataset['CODE_BEPALING'].iloc[i] == key:

                lst.append(dataset['UITSLAG'].iloc[i])
        biglist.append(lst)
        count += 1
        print (str(count) + '/' + str(len(keys)))
        
    print('done making lists')

    stats = np.zeros([len(keys),4])
    for i in range(len(keys)):
        
        # Turn strings into floats
        biglist[i] = list(np.float_(biglist[i]))
        
        # Express every number in standard score
        for i in range(len(a)):
            biglist[i][i] = (biglist[i][i] - np.mean(biglist[i]))/np.std(biglist[i])
            
        if len(biglist[i]) > 2:
            
            stats[i,0] = statistics.mean(list(np.float_(biglist[i])))
            stats[i,1] = statistics.median(list(np.float_(biglist[i])))
            stats[i,2] = statistics.stdev(list(np.float_(biglist[i])))
            stats[i,3] = statistics.variance(list(np.float_(biglist[i])))   

    return biglist, stats

biglist_uitslagen, stats = data_spreadings(mini_data)
