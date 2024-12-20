import pandas as pd
from utils.logger import logger

def data_ingestion(file_path):
    try:
        logger.info(f"Reading data from {file_path}")
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        logger.error(f"Error in data ingestion: {e}")
        raise e


