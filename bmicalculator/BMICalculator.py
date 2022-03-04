import time
import numpy as np
import pandas as pd
import yaml
import json


class BMICalculator:   
    
    def __init__(self,cfg_path):#, file_path):
        
        #loading config from yaml file 
        self.config=self.yaml_load(cfg_path)
        
        #extending bmi bins from -inf to inf
        self.bmi_bins = self.extendBins(self.config['bmi_bins'])
        
        #assigning config values to class object
        self.bmi_category = self.config['bmi_category']
        self.health_risk_category = self.config['health_risk_category']
        
        #reading json data into dataframe
        self.df= self.readData(self.config['data_dir'])
        
        # creating BMICategory feature
        self.df['BMICategory'] = self.getBMICategories()
        
        # creating HealthRiskCategory feature
        self.df['HealthRiskCategory']=self.getHealthRiskCategories()
    
    @staticmethod
    def yaml_load(path : str) -> dict:
        """Reads a yaml file and coverts it to dictionary."""
        try:
            with open(path) as f:
                config = yaml.safe_load(f)
        except Exception as ex:
            print(ex)
            exit(1)
        return config
    
    @staticmethod
    def extendBins(bmi_bins : list) -> list:
        '''
         extending bmi bins from -inf to inf
         
        '''
        cfg_copy=[]
        cfg_copy.append(-np.inf)
        cfg_copy.extend(bmi_bins )
        cfg_copy.append(np.inf)
        
        return cfg_copy
    
    def readData(self,data_path: str) -> pd.DataFrame:
        '''
        Reads data from json file and performs data prepartions
        
        '''
        try :
            with open(data_path) as f:
                data=[json.loads(line) for line in f.read().splitlines()]
        except Exception as ex:
            print(ex)
            exit(0)
        try:
            data=pd.DataFrame(data)
        except Exception as ex:
            print(ex)
            print('Cannot convert json into dataframe, please check the data file')
            exit(0)
            
        data=self.dataprep(data.copy())
        
        return data
    
    @staticmethod
    def dataprep(df:pd.DataFrame) -> pd.DataFrame:
        '''
        Creating features from Data

        '''
        try:
            print('Converting Height from CM -> M')
            df['HeightM']= df.apply(lambda x: (x['HeightCm'] /100),axis=1)
        except Exception as ex:
            print(ex)
            exit(0)
        try :
            print('Calculating BMI,BMI(kg/m2) = mass(kg) / height(m)**2')
            df['BMI'] = df.apply(lambda x: (x['WeightKg'] /x['HeightM']),axis=1)
            # rounding BMI values to 2
            df['BMI'] = df['BMI'].apply(lambda x: round(x, 2)) 
        except ZeroDivisionError:
            print("Height column has o values, cant compute BMI")
            exit(0)
        except Exception as ex:
            print(ex)
            exit(0)

        return df

    def getBMICategories(self) -> pd.Series:
        '''
        Creating feature : BMICategories

        Input : Dataframe with calculated BMI
        Output: Dataframe with categorized BMI values

        '''
        try :
            cat_df = pd.cut(self.df['BMI'], bins=self.bmi_bins, include_lowest=False, labels=self.bmi_category)
        except Exception as ex:
            print(ex)
            exit(1)
        return cat_df
    
    def getHealthRiskCategories(self) -> pd.Series:
        '''
        Creating feature : HealthRiskCategory

        Input : Dataframe with calculated BMI
        Output: Dataframe with categorized HealthRisk values

        '''
        try :
            cat_df = pd.cut(self.df['BMI'], bins=self.bmi_bins, include_lowest=False, labels=self.health_risk_category)
        except Exception as ex:
            print(ex)
            exit(1)
        return cat_df

    @property
    def getBMIBins(self):
        return self.bmi_bins
    @property
    def getBMICategory(self):
        return self.bmi_category
    @property
    def getHealthRiskCategory(self):
        return self.health_risk_category
    @property
    def getOverWeightCount(self):
        try:
            print('Total Overweighted people records: ',np.sum(self.df['BMICategory']=='Overweight'))
        except Exception as ex:
            print(ex)
    @property      
    def getSeverelyObese(self):
        try:
            print('Total Severely obese people records: ',np.sum(self.df['BMICategory']=='Severely obese'))
        except Exception as ex:
            print(ex)
    @property    
    def getVerySeverelyObese(self):
        try:
            print('Total Very Severely obese people records: ',np.sum(self.df['BMICategory']=='Very severely obese'))
        except Exception as ex:
            print(ex)
