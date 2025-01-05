# Databricks notebook source
# MAGIC %md
# MAGIC # Environment Setup: Installing and importing required libraries

# COMMAND ----------

from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder \
    .appName("NYC Taxi Fare Prediction") \
    .getOrCreate()

print("Environment setup completed.")

