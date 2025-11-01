# it loads raw data, splits it into train/test sets, 
# and saves them for further preprocessing and model training.

import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd


from sklearn.model_selection import train_test_split

from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig
from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer

@dataclass #it uses the @dataclass decorator → Python will automatically create an __init__ method.

class DataIngestionConfig: # It defines three default file paths:
  train_data_path: str=os.path.join('artifacts',"train.csv") # train_data_path → where your training data will be saved.
  test_data_path: str=os.path.join('artifacts',"test.csv")# test_data_path → where your test data will be saved.
  raw_data_path: str=os.path.join('artifacts',"data.csv")# raw_data_path → where your original full dataset will be saved.
# All files are stored inside an artifacts/ folder, a common convention for ML projects.




class DataIngestion:
  # self.ingestion_config creates an instance of DataIngestionConfig 
  # so you can access its paths (like self.ingestion_config.train_data_path).
  def __init__(self):
    self.ingestion_config=DataIngestionConfig()

# Defines the main function that performs ingestion.
# Logs the start of the process (good for debugging
#  and monitoring your ML pipeline).
  def initiate_data_ingestion(self):
    logging.info("Entered the data ingestion method or component")
    try:
      # Reads your raw dataset (stud.csv) located inside the notebook/data directory
      df=pd.read_csv(r'notebook\data\stud.csv') 
      logging.info('Read the dataset as dataframe') 


      os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
      df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
      logging.info("Train Test Split initiated")

      train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

      train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
      test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

      logging.info("Ingestion of data is completed")


      return(
        self.ingestion_config.train_data_path,
        self.ingestion_config.test_data_path,

      )

    except Exception as e:
      raise CustomException(e,sys)
    

if __name__=="__main__":
  obj=DataIngestion()
  train_data,test_data=obj.initiate_data_ingestion()
   
  data_tranformation=DataTransformation()
  train_arr,test_arr,_=data_tranformation.initiate_data_transformation(train_data,test_data)


  modeltrainer=ModelTrainer()
  print(modeltrainer.initiate_model_trainer(train_arr,test_arr))
  
