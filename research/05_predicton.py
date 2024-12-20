from utils.logger import logger

def make_predictions(model, new_data):
    try:
        logger.info("Making predictions on new data...")
        predictions = model.predict(new_data)
        return predictions
    except Exception as e:
        logger.error(f"Error in making predictions: {e}")
        raise e
