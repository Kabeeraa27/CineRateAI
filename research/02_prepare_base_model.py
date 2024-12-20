from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from utils.logger import logger

def data_transformation(data, target_column):
    try:
        logger.info("Starting data transformation process...")
        
        # Splitting features and target
        X = data.drop(columns=[target_column])
        y = data[target_column]

        # Train-test split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Feature scaling
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        return X_train_scaled, X_test_scaled, y_train, y_test
    except Exception as e:
        logger.error(f"Error in data transformation: {e}")
        raise e


