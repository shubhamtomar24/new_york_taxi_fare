import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    """Load raw data from a CSV file."""
    return pd.read_csv(file_path)

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean raw data by handling missing values and outliers."""
    df = df.dropna()  # Drop rows with missing values
    # Add custom cleaning logic here
    return df