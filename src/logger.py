import logging
import os 
from datetime import datetime

# ✅ Just create the log filename, without extra dot
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# ✅ Create a proper 'logs' directory
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

# ✅ Create full path to log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# ✅ Logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

