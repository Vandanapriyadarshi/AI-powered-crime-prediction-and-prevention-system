from pyspark.sql.functions import col
import asyncio
from alert_server import send_alerts  # Make sure alert_server.py defines send_alerts()
#from pyspark.sql.functions import col
import asyncio
from alert_server import send_alerts
# 🔹 Save to Console
def write_to_console(df):
    return df.writeStream \
        .outputMode("append") \
        .format("console") \
        .start()

# 🔹 Save to Parquet File
def write_to_file(df):
    return df.writeStream \
        .outputMode("append") \
        .format("parquet") \
        .option("path", "crime_data/") \
        .option("checkpointLocation", "checkpoints/") \
        .start()

# 🔹 Save to PostgreSQL Database
def write_to_db(batch_df, batch_id):
    batch_df.write \
        .format("jdbc") \
        .option("url", "jdbc:postgresql://localhost:5432/crime_db") \
        .option("dbtable", "crime_reports") \
        .option("user", "postgres") \
        .option("password", "your_password") \
        .mode("append") \
        .save()

# 🔔 Send Real-Time Alerts via WebSocket
# def alert_if_needed(batch_df, batch_id):
#     high_alerts = batch_df.filter(col("severity") == "High")
#     if high_alerts.count() > 0:
#         alert_data = high_alerts.toPandas().to_dict(orient="records")
#         asyncio.run(send_alerts(alert_data))
def alert_if_needed(batch_df, batch_id):
    high_alerts = batch_df.filter(col("severity") == "High")
    if high_alerts.count() > 0:
        alert_data = high_alerts.toPandas().to_dict(orient="records")
        asyncio.run(send_alerts(alert_data))