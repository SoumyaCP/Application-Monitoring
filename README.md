📊 Application Monitoring Dashboards
📝 Project Overview
This project implements a comprehensive Log Analytics Platform designed to collect, process, and visualize log data in real-time. It leverages Apache Kafka ⚡ for real-time log ingestion, a relational database 🗄️ for storing processed logs, and Grafana 📈 for dynamic visualization of key application metrics.

🌟 Features
🔢 Request Count per Endpoint: Tracks the number of requests made to each API endpoint and visualizes it.

⏱️ Response Time Trends: Displays trends and patterns in response times over various time periods.

❗ Most Frequent Errors: Highlights recurring errors in the application for easier troubleshooting.

🟢 Real-Time Logs: Provides a live feed of logs to monitor application behavior in real-time.

🛠️ Technology Stack
🐳 Docker – Containerization of all components

⚡ Apache Kafka – Scalable, real-time log ingestion

🗄️ PostgreSQL/MySQL – Structured log storage

📊 Grafana – Visualization of log data

🌐 REST API Server – Simulates workload via 5–10 endpoints

🔄 Kafka Log Producer/Consumer – Log pipeline to database

🚀 Implementation Summary
✅ Developed a REST API server with multiple endpoints to simulate real workloads and generate logs.

✅ Configured Apache Kafka with multiple topics to ingest different types of logs in real-time.

✅ Built a Kafka producer that pushes API-generated logs into Kafka topics.

✅ Set up Docker containers for API server, Kafka, Zookeeper, database, and Grafana for easy deployment.

✅ Implemented a Kafka consumer that reads, processes, and stores logs into the relational database.

✅ Designed interactive Grafana dashboards to visualize:

🔢 Request counts

⏱️ Response times

❗ Frequent errors

🟢 Real-time logs

✅ Integrated monitoring and alerting mechanisms for proactive incident response.
