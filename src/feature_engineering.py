import pandas as pd

def add_features(df: pd.DataFrame) -> pd.DataFrame:
    """Add custom features to the dataset."""
    df['hour'] = pd.to_datetime(df['pickup_datetime']).dt.hour
    df['day_of_week'] = pd.to_datetime(df['pickup_datetime']).dt.dayofweek
    return df
