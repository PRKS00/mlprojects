import logging
import os
from datetime import datetime


LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" #Creates a log file name with the current date and time.
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE) 
#Builds a path for where your log files will be stored.
# os.getcwd() → gives the current working directory
# "logs" → folder name for logs
# LOG_FILE → the file name created above


os.makedirs(logs_path,exist_ok=True) #Creates the directory path where logs will be stored.


LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)


logging.basicConfig(
  filename=LOG_FILE_PATH,
  format="[%(asctime)s] %(lineno)d %(name)s-%(levelname)s-%(message)s",
  level=logging.INFO,


)
