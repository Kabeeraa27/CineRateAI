from sklearn.metrics import mean_squared_error
from utils.logger import logger

def train_model(model, X_train, y_train):
    try:
        logger.info("Training the model...")

        # Training the model on the training data
        model.fit(X_train, y_train)
        logger.info("Model training completed.")
        return model

    except Exception as e:
        logger.error(f"Error during model training: {e}")
        raise e

def evaluate_model(model, X_test, y_test):
    try:
        logger.info("Evaluating the model...")

        # Predicting on the test data
        y_pred = model.predict(X_test)

        # Calculating the performance using Mean Squared Error
        mse = mean_squared_error(y_test, y_pred)
        logger.info(f"Model evaluation completed. MSE: {mse}")
        return mse

    except Exception as e:
        logger.error(f"Error during model evaluation: {e}")
        raise e
