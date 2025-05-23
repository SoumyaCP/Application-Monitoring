import time
import random
import requests

endpoints = [
    "http://api:5000/api/v1/products",
    "http://api:5000/api/v1/orders",
    "http://api:5000/api/v1/users",
    "http://api:5000/api/v1/login",
    "http://api:5000/api/v1/logout",
]

while True:
    endpoint = random.choice(endpoints)
    try:
        response = requests.get(endpoint) if "GET" in endpoint else requests.post(endpoint)
        print(f"Hit {endpoint} -> Status: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")
    time.sleep(1)

