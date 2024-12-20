from utils.logger import logger

def make_predictions(model, new_data):
    try:
        logger.info("Making predictions on new data...")

        # Predicting the audience ratings
        predictions = model.predict(new_data)
        
        logger.info("Predictions made successfully.")
        return predictions

    except Exception as e:
        logger.error(f"Error in making predictions: {e}")
        raise e
