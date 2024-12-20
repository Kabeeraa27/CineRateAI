import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from utils.logger import logger

def prepare_base_model(data):
    try:
        logger.info("Preparing base model for prediction...")

        # Assuming 'target' column is the audience rating
        features = data.drop('target', axis=1)  # Drop the target column
        target = data['target']  # Audience rating column

        # Splitting the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
        
        # Initializing the base model (RandomForestRegressor)
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        
        logger.info("Base model prepared.")
        return model, X_train, X_test, y_train, y_test

    except Exception as e:
        logger.error(f"Error in preparing the base model: {e}")
        raise e
