import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from utils.logger import logger
from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split

# Define your models dictionary
models = {
    'LinearRegression': LinearRegression(),
    'RandomForest': RandomForestRegressor(n_estimators=100, random_state=42),
    'DecisionTree': DecisionTreeRegressor(random_state=42),
    'SupportVectorRegressor': SVR(),
    'GradientBoosting': GradientBoostingRegressor(random_state=42),
    'Lasso': Lasso(alpha=0.1, random_state=42),
    'Ridge': Ridge(alpha=0.1, random_state=42),
    'ElasticNet': ElasticNet(alpha=0.1, l1_ratio=0.5, random_state=42),
    'KNeighbors': KNeighborsRegressor(n_neighbors=5)
}

def evaluate_model(model, X_test, y_test):
    try:
        logger.info("Evaluating model performance...")

        # Making predictions using the trained model
        y_pred = model.predict(X_test)

        # Mean Absolute Error
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)

        logger.info(f"Evaluation complete. MAE: {mae}, R2: {r2}")
        return mae, r2

    except Exception as e:
        logger.error(f"Error in model performance evaluation: {e}")
        raise e

# Data loading and splitting
def prepare_data(data):
    # Split the data into features (X) and target (y)
    X = data.drop(columns=['target_column'])  # Replace 'target_column' with your actual target column name
    y = data['target_column']  # Replace with your actual target column name

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

# Results dictionary to store evaluation metrics
results = {}

# Function to evaluate all models
def evaluate_all_models(data):
    X_train, X_test, y_train, y_test = prepare_data(data)

    # Loop through each model and evaluate
    for model_name, model in models.items():
        # Create a pipeline with scaling and the model
        pipeline = Pipeline([
            ('scaler', StandardScaler()),  # Scaling the data
            ('model', model)
        ])

        # Fit the pipeline on the training data
        pipeline.fit(X_train, y_train)

        # Predict and calculate metrics
        y_pred = pipeline.predict(X_test)
        
        mae = mean_absolute_error(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        r2 = r2_score(y_test, y_pred)
        
        # Store the results
        results[model_name] = {
            'Mean Absolute Error': mae,
            'Mean Squared Error': mse,
            'Root Mean Squared Error': rmse,
            'R^2 Score': r2
        }

    # Convert results to DataFrame for easy viewing
    results_df = pd.DataFrame(results).T
    print(results_df)

