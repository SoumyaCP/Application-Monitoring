import json
import psycopg2
import time
from kafka import KafkaConsumer
from kafka.errors import NoBrokersAvailable


while True:
    try:
        conn = psycopg2.connect(
            dbname='loganalytics',
            user='loguser',
            password='logpass',
            host='postgres',
            port='5432'
        )
        print("✅ Connected to PostgreSQL!")
        break
    except psycopg2.OperationalError:
        print("❌ PostgreSQL not ready yet. Retrying in 5 seconds...")
        time.sleep(5)

cursor = conn.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS logs (
        id SERIAL PRIMARY KEY,
        timestamp TIMESTAMP,
        status INTEGER,
        message TEXT,
        endpoint TEXT
    );
""")
conn.commit()


while True:
    try:
        consumer = KafkaConsumer(
            'success-logs', 'log-400', 'log-401', 'log-403', 'log-404', 'log-405', 'log-500',
            bootstrap_servers='kafka:9092',
            auto_offset_reset='earliest',
            group_id='log-consumer-group',
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )
        print("✅ Connected to Kafka!")
        break
    except NoBrokersAvailable:
        print("❌ Kafka not ready yet. Retrying in 5 seconds...")
        time.sleep(5)

print("📡 Consumer is running and listening to Kafka topics...")

for msg in consumer:
    log = msg.value
    print("📥 Log received:", log)

    cursor.execute(
        "INSERT INTO logs (timestamp, status, message, endpoint) VALUES (%s, %s, %s, %s)",
        (
            log.get("timestamp"),
            log.get("status"),
            f"Status Code: {log.get('status')}",
            log.get("endpoint")
        )
    )
    conn.commit()
    print("✅ Log inserted into PostgreSQL")

