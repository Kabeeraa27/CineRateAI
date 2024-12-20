from sklearn.linear_model import LinearRegression
from utils.logger import logger

def train_model(X_train, y_train):
    try:
        logger.info("Training Linear Regression model...")
        model = LinearRegression()
        model.fit(X_train, y_train)
        return model
    except Exception as e:
        logger.error(f"Error in model training: {e}")
        raise e


