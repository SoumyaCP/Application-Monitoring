from flask import Flask, request, jsonify
from kafka import KafkaProducer
import json
from datetime import datetime
import time
from kafka.errors import NoBrokersAvailable

app = Flask(__name__)

while True:
    try:
        producer = KafkaProducer(
            bootstrap_servers='kafka:9092',
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        print("Connected to Kafka!")
        break
    except NoBrokersAvailable:
        print("Kafka not ready, retrying in 5 seconds...")
        time.sleep(5)


def log_request(endpoint, status):
    log = {
        "endpoint": endpoint,
        "status": status,
        "timestamp": datetime.utcnow().isoformat()
    }

    status_str = str(status)
    if status_str.startswith("2"):
        topic = "success-logs"
    elif status_str.startswith("4") or status_str.startswith("5"):
        topic = f"log-{status_str}"
    else:
        topic = "other-logs"

    producer.send(topic, log)
    producer.flush()


@app.route("/api/v1/products", methods=["GET"])
def get_products():
    log_request("/api/v1/products", 200)
    return jsonify({"message": "List of products"}), 200

@app.route("/api/v1/orders", methods=["POST"])
def create_order():
    log_request("/api/v1/orders", 201)
    return jsonify({"message": "Order created"}), 201

@app.route("/api/v1/users", methods=["GET"])
def get_users():
    log_request("/api/v1/users", 200)
    return jsonify({"message": "List of users"}), 200

@app.route("/api/v1/login", methods=["POST"])
def login():
    log_request("/api/v1/login", 200)
    return jsonify({"message": "User logged in"}), 200

@app.route("/api/v1/logout", methods=["POST"])
def logout():
    log_request("/api/v1/logout", 200)
    return jsonify({"message": "User logged out"}), 200


@app.route("/api/v1/badrequest", methods=["GET"])
def bad_request():
    log_request("/api/v1/badrequest", 400)
    return jsonify({"error": "Bad Request"}), 400

@app.route("/api/v1/unauthorized", methods=["GET"])
def unauthorized():
    log_request("/api/v1/unauthorized", 401)
    return jsonify({"error": "Unauthorized"}), 401

@app.route("/api/v1/forbidden", methods=["GET"])
def forbidden():
    log_request("/api/v1/forbidden", 403)
    return jsonify({"error": "Forbidden"}), 403

@app.route("/api/v1/server-error", methods=["GET"])
def server_error():
    log_request("/api/v1/server-error", 500)
    return jsonify({"error": "Internal Server Error"}), 500


@app.errorhandler(404)
def not_found(e):
    log_request(request.path, 404)
    return jsonify({"error": "Not Found"}), 404

@app.errorhandler(405)
def method_not_allowed(e):
    log_request(request.path, 405)
    return jsonify({"error": "Method Not Allowed"}), 405

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

