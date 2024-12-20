# research/model_evaluation_04.py
from sklearn.metrics import mean_absolute_error, r2_score
from utils.logger import logger

def evaluate_model(model, X_test, y_test):
    try:
        logger.info("Evaluating model performance...")

        # Making predictions using the trained model
        y_pred = model.predict(X_test)

        # Mean Absolute Error
        mae = mean_absolute_error(y_test, y_pred)

        # R-squared score
        r2 = r2_score(y_test, y_pred)

        logger.info(f"Evaluation complete. MAE: {mae}, R2: {r2}")
        return mae, r2

    except Exception as e:
        logger.error(f"Error in model performance evaluation: {e}")
        raise e
