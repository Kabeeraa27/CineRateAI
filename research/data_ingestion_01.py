import os
import pandas as pd
from utils.logger import get_logger

logger = get_logger(__name__)

def data_ingestion(input_path, artifacts_folder):
    logger.info("Starting data ingestion...")
    os.makedirs(artifacts_folder, exist_ok=True)
    try:
        data = pd.read_excel(input_path)
        output_path = os.path.join(artifacts_folder, "data.csv")
        data.to_csv(output_path, index=False)
        logger.info(f"Data saved to {output_path}")
    except Exception as e:
        logger.error(f"Error in data ingestion: {e}")
        raise


