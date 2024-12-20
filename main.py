# main.py
from utils.logger import logger
from research.data_ingestion_01 import data_ingestion
from research.prepare_base_model_02 import prepare_base_model
from research.model_training_03 import train_model
from research.model_evaluation_04 import evaluate_model
from research.prediction_05 import make_predictions

def main():
    try:
        # Data Ingestion
        logger.info("Starting data ingestion process...")
        data = data_ingestion("C:/DATASETS/Rotten_Tomatoes_Movies3.xls")  # Example file path or link
        
        # Prepare Base Model
        logger.info("Preparing base model...")
        base_model = prepare_base_model()
        
        # Model Training
        logger.info("Training the model...")
        trained_model = train_model(base_model, data)
        
        # Model Evaluation
        logger.info("Evaluating the model...")
        evaluation_results = evaluate_model(trained_model, data)
        logger.info(f"Evaluation Results: {evaluation_results}")
        
        # Making Predictions
        logger.info("Making predictions...")
        new_data = data.sample(10)  # Example: Make predictions on a random sample of data
        predictions = make_predictions(trained_model, new_data)
        
        logger.info(f"Predictions: {predictions}")
        
    except Exception as e:
        logger.error(f"An error occurred during the process: {e}")
        raise e


if __name__ == "__main__":
    main()
