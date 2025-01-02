import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def train_model(df: pd.DataFrame, target_col: str):
    """Train a Random Forest model."""
    logging.info("Starting model training...")
    
    # Prepare features and target
    X = df.drop(columns=[target_col])
    y = df[target_col]

    # Split the data
    logging.info("Splitting the data into training and test sets.")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    logging.info("Training the Random Forest model.")
    model = RandomForestRegressor()
    model.fit(X_train, y_train)

    # Evaluate the model
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    logging.info(f"Mean Squared Error: {mse}")

    logging.info("Model training completed.")
    return model
