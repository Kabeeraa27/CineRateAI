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
        
        if data is None or data.empty:
            raise ValueError("Data ingestion failed, the dataset is empty or incorrect.")
        
        # Prepare Base Model
        logger.info("Preparing base model...")
        X_train, X_test, y_train, y_test = prepare_base_model(data)  # Pass the data to the function
        
        if X_train is None or X_test is None or y_train is None or y_test is None:
            raise ValueError("Base model preparation failed.")
        
        # Model Training (Training all models)
        logger.info("Training all models...")
        trained_models = train_model(X_train, y_train)  # Only pass X_train and y_train

        if not trained_models:
            raise ValueError("Model training failed.")
        
        # Model Evaluation
        logger.info("Evaluating models...")
        for model_name, trained_model in trained_models.items():
            evaluation_results = evaluate_model(trained_model, X_test, y_test)  # Pass correct parameters for evaluation
            logger.info(f"Evaluation Results for {model_name}: {evaluation_results}")
        
        # Making Predictions
        logger.info("Making predictions...")
        new_data = data.sample(10)  # Example: Make predictions on a random sample of data
        for model_name, trained_model in trained_models.items():
            predictions = make_predictions(trained_model, new_data)
            logger.info(f"Predictions from {model_name}: {predictions}")
        
    except Exception as e:
        logger.error(f"An error occurred during the process: {e}")
        raise e


if __name__ == "__main__":
    main()
