# stream_reader.py
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType

def create_spark_session():
    return SparkSession.builder \
        .appName("CrimePredictionStream") \
        .master("local[*]") \
        .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.1") \
        .getOrCreate()

def read_from_kafka(spark):
    schema = StructType().add("report", StringType()).add("location", StringType())

    df = spark.readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "localhost:9092") \
        .option("subscribe", "police_reports") \
        .option("startingOffsets", "earliest") \
        .load()

    json_df = df.selectExpr("CAST(value AS STRING)") \
        .select(from_json(col("value"), schema).alias("data")) \
        .select("data.*")

    return json_df
