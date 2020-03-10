# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 16:06:56 2020

@author: Jim Smit
"""

# Functions


import numpy as np
import pandas as pd
import math




def data_cleaner(file_name,n=0):
    """
    Code takes raw CSV file as input, converges to clean pandas Dataframe

    Inputs: raw dataset
            number of samples to take, default is all.
    Returns: Pd Dataframe

    """
    if n == 0:
        data = pd.read_csv(file_name,sep='";"',engine='python')
    else:
        data = pd.read_csv(file_name,nrows = n, sep='";"',engine='python')  # values seperated by ";"
    
    
    
    data = data[data['UITSLAG'].notna()]      # delete all smaples without test value
    
    data['UITSLAG'] = data['UITSLAG'].apply(lambda x: x.replace(',','.'))  # replace all comma sperated value by periods
    
    return data




def counter(dataset):
    """
    Function counts total of tests for specific department (axis 0) and for every test type 
    specifically (axis 1)

    Parameters
    ----------
    dataset : Takes as input cleaned dataset

    Returns
    -------
    df : pandas dataframe with departments divided over cl=olumns and test types over rows

    """
    print('counter started')
    # Number of samples
    n_samples = dataset.shape[0]
    
    #Unique departments
    departments = dataset.CODE_AFD.unique()
    
    keys = dataset.CODE_BEPALING.unique()
    values = dataset.NAAM_BEPALING.unique()
    
    M = np.zeros([keys.shape[0],departments.shape[0]])
    
    biglist = []
    count = 0
    for department in departments:
        lst = list()
        for i in range(n_samples):
            if dataset['CODE_AFD'].iloc[i]== department:
                lst.append(dataset['CODE_BEPALING'].iloc[i])
        biglist.append(lst)
        count += 1
        if count%10 == 1:
            print(str(count) + '/' + str(len(departments)))
        
    print('done making lists')
    
    dep_count = 0
    for lst in biglist:
        key_count = 0
        for key in keys:
            a = lst.count(key)
            M[key_count,dep_count] = a
            key_count += 1
        dep_count += 1
        if dep_count%10 == 1:
            print(str(dep_count) + '/' + str(len(departments)))


    df = pd.DataFrame(M,index=keys)
    df.columns = departments
    
    return df