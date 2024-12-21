from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
from utils.logger import logger

def train_model(X_train, y_train):
    try:
        logger.info("Training the models...")

        # Dictionary of available models
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

        trained_models = {}

        # Loop over each model and train it
        for model_name, model in models.items():
            logger.info(f"Training {model_name}...")
            model.fit(X_train, y_train)
            trained_models[model_name] = model
            logger.info(f"{model_name} training completed.")

        return trained_models

    except Exception as e:
        logger.error(f"Error during model training: {e}")
        raise e
