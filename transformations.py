# transformations.py

from pyspark.sql.functions import col, udf
from pyspark.sql.types import StringType
from joblib import load

# Load the trained ML model
model = load("crime_severity_model.joblib")

# Define a UDF to apply model prediction
def predict_severity(report_text):
    return model.predict([report_text])[0]

# Register the UDF with Spark
severity_udf = udf(predict_severity, StringType())

# Apply transformations
def apply_transformations(df):
    # Filter out rows without location
    filtered_df = df.filter(col("location").isNotNull())

    # Add severity column using ML model
    enriched_df = filtered_df.withColumn("severity", severity_udf(col("report")))

    return enriched_df
