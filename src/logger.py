import logging
import os
from datetime import datetime

# Define log file path
LOG_DIR = "logs"
LOG_FILE = f"{datetime.now().strftime('%m%d%Y__%H%M%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

# Create logs directory if it doesn't exist
os.makedirs(LOG_DIR, exist_ok=True)

# Configure logging (FIXED: Changed 'forat' to 'format')
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="%(asctime)s %(levelname)s %(message)s",  # Fixed typo here
    level=logging.INFO
)

if __name__=="__main__":
    logging.info("Logging has started")
