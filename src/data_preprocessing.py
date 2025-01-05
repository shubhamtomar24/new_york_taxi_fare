def load_data(file_path):
    """
    Load NYC Taxi dataset from a CSV file.
    
    Parameters:
        file_path (str): Path to the CSV file.
        
    Returns:
        DataFrame: Spark DataFrame containing the loaded data.
    """
    print(f"Loading data from: {file_path}...")
    
    # Read CSV file with schema inference
    spark_df = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load(file_path)
    
    # Rename columns to match Spark's naming conventions if necessary
    spark_df = spark_df.withColumnRenamed("pickup_datetime", "pickup_datetime") \
                       .withColumnRenamed("fare_amount", "fare_amount") \
                       .withColumnRenamed("passenger_count", "passenger_count")
    
    print(f"Loaded {spark_df.count()} rows from {file_path}.")
    return spark_df