import requests
import time

BASE_URL = "http://localhost:5000"

endpoints = [
    ("/api/v1/products", "GET"),
    ("/api/v1/orders", "POST"),
    ("/api/v1/users", "GET"),
    ("/api/v1/login", "POST"),
    ("/api/v1/logout", "POST"),
    ("/api/v1/badrequest", "GET"),
    ("/api/v1/unauthorized", "GET"),
    ("/api/v1/forbidden", "GET"),
    ("/api/v1/server-error", "GET"),
    ("/api/v1/nonexistent", "GET"),        
    ("/api/v1/login", "PUT"),              
]

for i in range(50): 
    for path, method in endpoints:
        url = f"{BASE_URL}{path}"
        try:
            if method == "GET":
                res = requests.get(url)
            elif method == "POST":
                res = requests.post(url)
            elif method == "PUT":
                res = requests.put(url)
            print(f"{method} {url} --> {res.status_code}")
        except Exception as e:
            print(f"Failed to hit {url}: {e}")
        time.sleep(0.2)  

