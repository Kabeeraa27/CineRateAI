from pipeline.data_ingestion import data_ingestion
from pipeline.data_transformation import data_transformation
from pipeline.model_training import train_model
from pipeline.model_evaluation import evaluate_model
from utils.logger import logger

if __name__ == "__main__":
    try:
        # File path and target column
        file_path = "artifacts/data_ingestion/dataset.csv"
        target_column = "target"  # Replace with actual target column name

        # Data ingestion
        data = data_ingestion(file_path)

        # Data transformation
        X_train, X_test, y_train, y_test = data_transformation(data, target_column)

        # Model training
        model = train_model(X_train, y_train)

        # Model evaluation
        evaluation_metrics = evaluate_model(model, X_test, y_test)

        logger.info(f"Pipeline completed successfully! Metrics: {evaluation_metrics}")
    except Exception as e:
        logger.error(f"Pipeline execution failed: {e}")
