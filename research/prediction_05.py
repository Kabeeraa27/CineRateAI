import pandas as pd
import joblib
import os
from utils.logger import get_logger

logger = get_logger(__name__)

def make_predictions(model_file, input_data_file, artifacts_folder):
    logger.info("Starting predictions...")
    try:
        # Load the model and feature names
        model = joblib.load(model_file)
        feature_names_path = os.path.join(artifacts_folder, 'feature_names.pkl')

        if os.path.exists(feature_names_path):
            feature_names = joblib.load(feature_names_path)
        else:
            logger.error(f"Feature names file {feature_names_path} not found.")
            raise FileNotFoundError(f"Feature names file {feature_names_path} not found.")

        # Read the input data for predictions
        input_data = pd.read_csv(input_data_file)

        text_columns = ['movie_info', 'movie_title', 'cast']
        input_data = input_data.drop(columns=[col for col in text_columns if col in input_data.columns], errors='ignore')

        # One-hot encode categorical columns
        columns_to_encode = ['rating', 'tomatometer_status']
        for col in columns_to_encode:
            if col in input_data.columns:
                input_data = pd.get_dummies(input_data, columns=[col], drop_first=True)

        # Select only numeric columns
        input_data = input_data.select_dtypes(include=['number'])

        # Ensure no target column (audience_rating) is in the input data
        if 'audience_rating' in input_data.columns:
            input_data = input_data.drop(columns=['audience_rating'])

        # Align the input data columns with the feature names used in training
        missing_cols = set(feature_names) - set(input_data.columns)
        for col in missing_cols:
            input_data[col] = 0  # Add missing columns with value 0

        input_data = input_data[feature_names]  # Reorder columns to match the model

        # Make predictions
        predictions = model.predict(input_data)
        input_data['predicted_audience_rating'] = predictions

        # Save predictions to output file
        output_file = os.path.join(artifacts_folder, "predictions.csv")
        input_data.to_csv(output_file, index=False)
        logger.info(f"Predictions saved to {output_file}")
    
    except Exception as e:
        logger.error(f"Error in making predictions: {e}")
        raise
