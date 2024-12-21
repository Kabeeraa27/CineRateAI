import pandas as pd
import os
from sklearn.impute import SimpleImputer
from category_encoders import TargetEncoder
from utils.logger import get_logger

logger = get_logger(__name__)

def prepare_base_model(input_file, artifacts_folder):
    logger.info("Starting data preparation...")
    try:
        data = pd.read_csv(input_file)

        # Fixing ratings
        rating_correction_map = {
            'PG-13)': 'PG-13',
            'NC17': 'NC-17',
            'R)': 'R'
        }
        data['rating'] = data['rating'].replace(rating_correction_map)

        # Convert date columns to datetime format
        date_columns = ['in_theaters_date', 'on_streaming_date']
        for col in date_columns:
            if col in data.columns:
                data[col] = pd.to_datetime(data[col], errors='coerce')

        # Extract year, month, day from 'in_theaters_date'
        if 'in_theaters_date' in data.columns:
            data['in_theaters_year'] = data['in_theaters_date'].dt.year
            data['in_theaters_month'] = data['in_theaters_date'].dt.month
            data['in_theaters_day'] = data['in_theaters_date'].dt.day

        # Calculate days_to_streaming
        if 'on_streaming_date' in data.columns and 'in_theaters_date' in data.columns:
            data['days_to_streaming'] = (data['on_streaming_date'] - data['in_theaters_date']).dt.days

        # Drop date columns
        data = data.drop(columns=['in_theaters_date', 'on_streaming_date'], errors='ignore')

        # Imputation for missing values
        numerical_features = data.select_dtypes(include=['number']).columns
        categorical_features = data.select_dtypes(include=['object']).columns
        num_imputer = SimpleImputer(strategy='mean')
        cat_imputer = SimpleImputer(strategy='most_frequent')

        # Impute missing values
        data[numerical_features] = num_imputer.fit_transform(data[numerical_features])
        data[categorical_features] = cat_imputer.fit_transform(data[categorical_features])

        # Apply target encoding for features
        target_encoder1 = TargetEncoder(cols=['cast', 'movie_info', 'movie_title'], smoothing=1.0)
        data[['cast', 'movie_info', 'movie_title']] = target_encoder1.fit_transform(data[['cast', 'movie_info', 'movie_title']], data['audience_rating'])

        # Apply custom target encoding for high-cardinality features
        target_encoder2 = TargetEncoder(cols=['genre', 'directors', 'writers', 'studio_name'], smoothing=5.0)
        data[['genre', 'directors', 'writers', 'studio_name']] = target_encoder2.fit_transform(data[['genre', 'directors', 'writers', 'studio_name']], data['audience_rating'])

        # One-Hot Encoding for categorical features
        data = pd.get_dummies(data, columns=['rating', 'tomatometer_status'], dtype=int)

        # Save cleaned data
        output_file = os.path.join(artifacts_folder, "cleaned_data.csv")
        data.to_csv(output_file, index=False)
        logger.info(f"Cleaned data saved to {output_file}")
    except Exception as e:
        logger.error(f"Error in data preparation: {e}")
        raise

