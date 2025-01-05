from data_preprocessing import load_data
from pyspark.sql.functions import col, year, month, dayofmonth
from databricks.feature_store import FeatureStoreClient

# Initialize Feature Store client
fs = FeatureStoreClient()

def engineer_features(table_path):
    """Load data, engineer features, and return the Spark DataFrame."""
    # Load data using the function from data_preprocessing.py
    spark_df = load_data(table_path)

    print("Engineering features...")
    spark_df = spark_df.withColumn("year", year(col("pickup_datetime")))
    spark_df = spark_df.withColumn("month", month(col("pickup_datetime")))
    spark_df = spark_df.withColumn("day", dayofmonth(col("pickup_datetime")))
    print("Feature engineering completed.")
    return spark_df

def save_features_to_store(spark_df, feature_table_name):
    """Save engineered features to the Databricks Feature Store."""
    print(f"Saving features to Feature Store: {feature_table_name}...")
    fs.create_table(
        name=feature_table_name,
        primary_keys=["pickup_datetime"],
        schema=spark_df.schema,
        description="Features for NYC Taxi Fare Prediction"
    )
    fs.write_table(feature_table_name, spark_df, mode="overwrite")
    print("Features saved to Feature Store.")

engineered_df = engineer_features("/Volumes/nyc_taxi_fare/default/data/train.delta")
save_features_to_store(engineered_df, "nyc_taxi.train_features")