
import json
import yaml
import pandas as pd
import numpy as np
from sys import exit

def testNanInList(test_list : list):
    '''
    test code for lists to check Nans
    '''
    if np.nan in test_list:
        print('list contains nans,cant process\nplease update the config')
        exit(1)
    else:
        print('Nan test success on the list')

def testStringsInList(test_list: list):
    '''
    test code for lists to check strings
    '''
    for item in test_list:
        if isinstance(item,str) :
            print('list contains strings,cant process\nplease update the config')
            print(item,test_list)
            exit(1)
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
    print('Lists are consistent for processing')

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

def doListTests(bin_list : list,bmi_category:list,health_risk_category: list):
    '''
    code for executing multiple tests
    
    '''
    for _list in [bin_list,bmi_category,health_risk_category]:
        testNanInList(_list)
        testDuplicatesInList(_list)
    testStringsInList(bin_list)
    testBinCounts(bin_list,bmi_category,health_risk_category)