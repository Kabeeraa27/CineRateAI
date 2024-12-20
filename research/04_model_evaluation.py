from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from utils.logger import logger

def evaluate_model(model, X_test, y_test):
    try:
        logger.info("Evaluating the model...")
        predictions = model.predict(X_test)
        mae = mean_absolute_error(y_test, predictions)
        mse = mean_squared_error(y_test, predictions)
        r2 = r2_score(y_test, predictions)

        logger.info(f"Model Evaluation:\nMAE: {mae}\nMSE: {mse}\nR2: {r2}")
        return {"mae": mae, "mse": mse, "r2": r2}
    except Exception as e:
        logger.error(f"Error in model evaluation: {e}")
        raise e
    
    