import pandas as pd
from src.data_preprocessing import load_data, clean_data

def test_load_data():
    """Test the data loading function."""
    df = load_data("data/sample.csv")
    assert isinstance(df, pd.DataFrame)

def test_clean_data():
    """Test the data cleaning function."""
    raw_data = {"col1": [1, None, 3], "col2": [4, 5, None]}
    df = pd.DataFrame(raw_data)
    clean_df = clean_data(df)
    assert clean_df.isnull().sum().sum() == 0
