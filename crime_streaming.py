# crime_streaming.py

from stream_reader import create_spark_session, read_from_kafka
from transformations import apply_transformations
from stream_writer import (
    write_to_console,
    write_to_file,
    write_to_db,
    alert_if_needed
)

if __name__ == "__main__":
    # Step 1: Create Spark session
    spark = create_spark_session()

    # Step 2: Read from Kafka
    raw_df = read_from_kafka(spark)

    # Step 3: Apply transformations (e.g., severity classification)
    transformed_df = apply_transformations(raw_df)

    # Step 4: Choose output sinks

    # 🔹 Output to console
    query_console = write_to_console(transformed_df)

    # 🔹 Save to Parquet files
    query_file = write_to_file(transformed_df)

    # 🔹 Save to PostgreSQL database
    query_db = transformed_df.writeStream.foreachBatch(write_to_db).start()

    # 🔹 Send real-time alerts (if severity == "High")
    query_alert = transformed_df.writeStream.foreachBatch(alert_if_needed).start()

    # Step 5: Keep the stream running
    query_console.awaitTermination()
    query_file.awaitTermination()
    query_db.awaitTermination()
    query_alert.awaitTermination()
