# Data ingestion is reading the dataset

'''
import os    # For doing level works like join, open, read. This os library is very important for Linux server
import sys   # For checkign any system error
from src.exception import CustomException   
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass                       # when we use dataclass then we dont need to use __init_() function for initializing variable just object of function created

'''

import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

## We are adding this after creating data_tranformation file 
from src.components.data_transformation import DataTransformation   

## Initialize Data Ingestion Configuration

@dataclass
class DataIngestionconfig:
    train_data_path:str=os.path.join('artifacts','train.csv')  # str is written after variable as to make it string  # artifacts is used for storing the output of the data which we are adding here through path
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_path:str=os.path.join('artifacts','raw.csv')


## Create Class for Data Ingestion

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionconfig()  # This variable has all the variables of dataingestion config data

    def initiate_data_ingestion(self):
        logging.info("Data Ingestion methods starts")
        try:
            df=pd.read_csv(os.path.join('notebooks/data','gemstone.csv')) # we can use os.path.join() inplace of ('./notebooks/data/gemstone.csv')
            logging.info('Dataset read as pandas Dataframe')
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)   # existe_ok will check if file is already there then it will not create again
            df.to_csv(self.ingestion_config.raw_data_path, index=True)

            logging.info('Train test split')
            train_set, test_set=train_test_split(df, test_size=0.30,random_state=42)   # we are using only two veriable here for taking the output and saving

            train_set.to_csv(self.ingestion_config.train_data_path,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,header=True)

            logging.info("Data Ingestion Completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )



        except Exception as e:
            logging.info("Exception occured at Data ingeation Stage")
            raise CustomException(e, sys)





