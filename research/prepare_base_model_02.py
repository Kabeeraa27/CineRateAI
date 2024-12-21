import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from category_encoders import TargetEncoder
from sklearn.impute import SimpleImputer
from utils.logger import logger

def feature_type(data):
    # Separate columns by data type
    numerical_features = data.select_dtypes(include=[np.number]).columns.tolist()
    categorical_features = data.select_dtypes(include=['object', 'category']).columns.tolist()
    datetime_features = data.select_dtypes(include=[np.datetime64]).columns.tolist()

    print(f"Numerical Columns ({len(numerical_features)}): \n", numerical_features)
    print()
    print(f"Categorical Columns ({len(categorical_features)}): \n", categorical_features)
    print()
    print(f"Datetime Columns ({len(datetime_features)}): \n", datetime_features)
    print()

def prepare_base_model(data, target_column='audience_rating'):
    try:
        logger.info("Preparing base model for prediction...")

        # Separate features and target
        features = data.drop(target_column, axis=1)
        target = data[target_column]

        # Impute missing values
        numerical_features = features.select_dtypes(include=[np.number]).columns.tolist()
        categorical_features = features.select_dtypes(include=['object', 'category']).columns.tolist()
        
        num_imputer = SimpleImputer(strategy='mean')
        cat_imputer = SimpleImputer(strategy='most_frequent')

        features[numerical_features] = num_imputer.fit_transform(features[numerical_features])
        features[categorical_features] = cat_imputer.fit_transform(features[categorical_features])

        # Encode categorical features
        features = feature_encoding(features)

        # Ensure that all features are numeric
        features = features.select_dtypes(include=[np.number])

        # Split data into train and test sets
        X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

        return X_train, X_test, y_train, y_test
        
    except Exception as e:
        logger.error(f"Error in preparing the base model: {e}")
        raise e


def feature_encoding(data):
    try:
        logger.info("Performing feature encoding...")

        # Check if 'audience_rating' exists in the data
        if 'audience_rating' not in data.columns:
            raise ValueError("'audience_rating' column is missing from the data")

        # Define features to apply different encoding methods
        te_features = ['cast', 'movie_info', 'movie_title']
        high_cardinal_features = ['genre', 'directors', 'writers', 'studio_name']
        ohe_features = ['rating', 'tomatometer_status']

        # Step 1: Applying Target Encoding to some features using category_encoders
        target_encoder1 = TargetEncoder(cols=te_features, smoothing=1.0)
        data[te_features] = target_encoder1.fit_transform(data[te_features], data['audience_rating'])

        # Step 2: Applying Custom Target Encoding to high-cardinality features
        target_encoder2 = TargetEncoder(cols=high_cardinal_features, smoothing=5.0)
        data[high_cardinal_features] = target_encoder2.fit_transform(data[high_cardinal_features], data['audience_rating'])

        # Step 3: Applying One-Hot Encoding to categorical features with low cardinality
        data = pd.get_dummies(data, columns=ohe_features, dtype=int)

        return data

    except Exception as e:
        logger.error(f"Error in feature encoding: {e}")
        raise e
