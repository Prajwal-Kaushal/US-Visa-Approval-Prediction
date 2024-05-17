import logging
import os

from from_root import from_root
from datetime import datetime 

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # instead of replacing same file, it will create differennt files with different timestamps, so that we have all the versions of the logs

log_dir = 'logs' # creating a logs folder in the root folder

logs_path = os.path.join(from_root(), log_dir, LOG_FILE) # joining the logs folder with the log file name to get the full path of the log file

os.makedirs(log_dir, exist_ok=True) # checking if the logs folder is already present or not, if not then create the folder


logging.basicConfig(
    filename=logs_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s", # format of the log file, firsr is the name of the log file and second is the level of the log file and third is the message of the log file.
    level=logging.DEBUG,
) # configuring the logger