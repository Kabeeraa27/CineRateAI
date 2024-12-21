import os
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import joblib
from category_encoders import TargetEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from utils.logger import get_logger

logger = get_logger(__name__)

def model_training(input_file, artifacts_folder):
    logger.info("Starting model training...")
    try:
        data = pd.read_csv(input_file)

        # Remove unnecessary columns
        if 'consensus' in data.columns:
            data.drop('consensus', axis=1, inplace=True)

        # Define target and features
        target = 'audience_rating'
        if target in data.columns:
            y = data[target]
            X = data.drop(columns=[target])

            # Ensure only numeric data is used for training
            X = X.select_dtypes(include=['number'])

            # Split data
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # Train models and evaluate
            models = {
                "LinearRegression": LinearRegression(),
                "RidgeRegression": Ridge(alpha=1.0),
                "LassoRegression": Lasso(alpha=0.1),
                "DecisionTreeRegressor": DecisionTreeRegressor(random_state=42),
                "RandomForestRegressor": RandomForestRegressor(n_estimators=100, random_state=42),
                "GradientBoostingRegressor": GradientBoostingRegressor(n_estimators=100, learning_rate=0.1)
            }

            results = {}
            for name, model in models.items():
                pipeline = Pipeline([
                    ('scaler', StandardScaler()),
                    ('model', model)
                ])

                # Fit the pipeline
                pipeline.fit(X_train, y_train)
                y_pred = pipeline.predict(X_test)

                # Calculate metrics
                mse = mean_squared_error(y_test, y_pred)
                rmse = np.sqrt(mse)
                mae = mean_absolute_error(y_test, y_pred)
                r2 = r2_score(y_test, y_pred)

                logger.info(f"{name} Metrics:")
                logger.info(f"  MSE: {mse}")
                logger.info(f"  RMSE: {rmse}")
                logger.info(f"  MAE: {mae}")
                logger.info(f"  R²: {r2}")
                logger.info("-" * 40)

                # Store the results
                results[name] = {
                    'Mean Absolute Error': mae,
                    'Mean Squared Error': mse,
                    'Root Mean Squared Error': rmse,
                    'R^2 Score': r2
                }

            # Identify the best model based on R² Score
            best_model_name = max(results, key=lambda model: results[model]['R^2 Score'])
            best_model_metrics = results[best_model_name]
            best_model = models[best_model_name]

            # Save the best model and feature names
            model_output_file = os.path.join(artifacts_folder, "best_model.pkl")
            feature_names_file = os.path.join(artifacts_folder, 'feature_names.pkl')
            
            feature_names = X.columns.tolist()  # Assuming X is your training dataframe

            # Save feature names to file
            joblib.dump(feature_names, feature_names_file)

            # Save the best model
            joblib.dump(best_model, model_output_file)
            logger.info(f"Best model saved to {model_output_file}")
            logger.info(f"Feature names saved to {feature_names_file}")
    except Exception as e:
        logger.error(f"Error in model training: {e}")
        raise
