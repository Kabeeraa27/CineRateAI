import os
import pandas as pd
import shutil
from utils.logger import logger

def data_ingestion(file_path, folder_path='artifacts'):
    try:
        # Create artifacts folder if it doesn't exist
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            logger.info(f"Created folder: {folder_path}")
        
        # Check if the provided file_path is a local file or URL
        if file_path.startswith('http') or file_path.startswith('www'):
            # If it's a URL, download it and save to the artifacts folder
            file_name = os.path.join(folder_path, file_path.split("/")[-1])
            logger.info(f"Downloading data from {file_path}")
            
            # Download the file using requests
            import requests
            response = requests.get(file_path)
            response.raise_for_status()  # Raise an exception for HTTP errors
            
            # Save the content to the artifacts folder
            with open(file_name, 'wb') as f:
                f.write(response.content)
                logger.info(f"File downloaded and saved as {file_name}")
            
            # Update the file_path to the saved file
            file_path = file_name

        # Check if the file exists locally (whether downloaded or already local)
        if not os.path.exists(file_path):
            logger.error(f"File does not exist: {file_path}")
            raise FileNotFoundError(f"File does not exist: {file_path}")

        # Copy the file to the 'artifacts' folder if it's not already there
        if not os.path.exists(os.path.join(folder_path, os.path.basename(file_path))):
            shutil.copy(file_path, folder_path)
            logger.info(f"File copied to artifacts folder: {file_path}")
        
        # Read the data based on file extension
        if file_path.endswith('.csv'):
            # Read the CSV file
            data = pd.read_csv(file_path)
            logger.info(f"Data successfully ingested from {file_path}")
            return data
        elif file_path.endswith('.xlsx') or file_path.endswith('.xls'):
            # Read the Excel file (both .xlsx and .xls formats)
            data = pd.read_excel(file_path, engine='xlrd')  # Use 'xlrd' for .xls files
            logger.info(f"Data successfully ingested from {file_path}")
            return data
        elif file_path.endswith('.json'):
            # Read the JSON file
            data = pd.read_json(file_path)
            logger.info(f"Data successfully ingested from {file_path}")
            return data
        else:
            logger.error(f"Unsupported file type: {file_path}")
            raise ValueError(f"Unsupported file type: {file_path}")
        
    except Exception as e:
        logger.error(f"Error in data ingestion: {e}")
        raise e
