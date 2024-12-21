import os
from research.data_ingestion_01 import data_ingestion
from research.prepare_base_model_02 import prepare_base_model
from research.model_training_03 import model_training
from research.prediction_05 import make_predictions
from utils.logger import get_logger

logger = get_logger(__name__)

if __name__ == "__main__":
    # Define paths
    input_path = "C:/DATASETS/Rotten_Tomatoes_Movies3.xls"
    artifacts_folder = "artifacts"
    os.makedirs(artifacts_folder, exist_ok=True)
    cleaned_data_file = os.path.join(artifacts_folder, "cleaned_data.csv")
    model_file = os.path.join(artifacts_folder, "best_model.pkl")

    try:
        # Step 1: Data Ingestion
        data_ingestion(input_path, artifacts_folder)

        # Step 2: Data Preparation
        prepare_base_model(os.path.join(artifacts_folder, "data.csv"), artifacts_folder)

        # Step 3: Model Training
        model_training(cleaned_data_file, artifacts_folder)

        # Step 4: Predictions
        make_predictions(model_file, cleaned_data_file, artifacts_folder)

        logger.info("Pipeline executed successfully!")
    except Exception as e:
        logger.error(f"Pipeline execution failed: {e}")
