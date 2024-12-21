from utils.logger import logger

def make_predictions(model, new_data):
    try:
        logger.info("Making predictions on new data...")

        # Log the shape of the new data for debugging purposes
        logger.info(f"New data shape: {new_data.shape}")

        # Predicting the audience ratings (or any other prediction task)
        predictions = model.predict(new_data)
        
        logger.info(f"Predictions made successfully. Predictions: {predictions[:5]}")  # Log first 5 predictions for preview
        return predictions

    except Exception as e:
        logger.error(f"Error in making predictions: {e}")
        raise e
