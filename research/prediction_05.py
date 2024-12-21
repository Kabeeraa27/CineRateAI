import pandas as pd
import joblib
from utils.logger import get_logger

logger = get_logger(__name__)

def make_predictions(model_file, input_data_file, artifacts_folder):
    logger.info("Starting predictions...")
    try:
        model = joblib.load(model_file)
        input_data = pd.read_csv(input_data_file)

        text_columns = ['movie_info', 'movie_title', 'cast']
        input_data = input_data.drop(columns=[col for col in text_columns if col in input_data.columns], errors='ignore')

        # Ensure the same columns used during training
        columns_to_encode = ['rating', 'tomatometer_status']
        for col in columns_to_encode:
            if col in input_data.columns:
                input_data = pd.get_dummies(input_data, columns=[col], drop_first=True)

        # Ensure only numerical columns are passed to the model
        input_data = input_data.select_dtypes(include=['number'])

        # Ensure no target column (audience_rating) is present in the input data during prediction
        if 'audience_rating' in input_data.columns:
            input_data = input_data.drop(columns=['audience_rating'])

        # Make predictions
        predictions = model.predict(input_data)
        input_data['predicted_audience_rating'] = predictions

        output_file = os.path.join(artifacts_folder, "predictions.csv")
        input_data.to_csv(output_file, index=False)
        logger.info(f"Predictions saved to {output_file}")
    except Exception as e:
        logger.error(f"Error in making predictions: {e}")
        raise


