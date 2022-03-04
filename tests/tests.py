
import json
import yaml
import pandas as pd
import numpy as np

def testNanInList(test_list : list):
    '''
    test code for lists to check Nans
    '''
    if np.nan in test_list:
        print('list contains nans,cant process\nplease update the config')
        return
    else:
        print('Nan test success on the list')

def testStringsInList(test_list: list):
    '''
    test code for lists to check strings
    '''
    for item in test_list:
        if ~isinstance(item,int):
            print('list contains strings,cant process\nplease update the config')
            return
    print('string test success on the list')

def testDuplicatesInList(test_list: list):
    '''
    test code for lists to duplicates
    '''
    list_copy=list(set(test_list))
    assert len(list_copy) == len(test_list), "Duplicates in the list,update the config"

def testBinCounts(bin_list : list,bmi_category:list,health_risk_category: list):
    '''
    test code checking consistency in list

    '''
    l1 = len(bin_list)
    l2 = len(bmi_category)
    l3 = len(health_risk_category)
    assert l1==l2-1,'bmi bins count should be less than categories'
    assert l1==l3-1,'bmi bins count should be less than categories'
    assert l2==l3,'bmi bins count should be less than categories'

def testCheckForColumns(df:pd.DataFrame):
    '''
    test code checking whether expected columns present in the data

    '''
    expected_cols =  ['HeightCm','Gender','WeightKg']
    
    if set(expected_cols).issubset(df.columns):
        print('All columnts present')
    else:
        print('Features missing in the input data,please check the data')
        exit(1)
