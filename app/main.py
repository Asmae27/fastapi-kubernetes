from fastapi import FastAPI
import socket

app = FastAPI(
    title="FastAPI Kubernetes Demo",
    description="First Kubernetes deployment",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Hello from FastAPI on Kubernetes!",
        "hostname": socket.gethostname()
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.get("/info")
def info():
    return {
        "application": "FastAPI",
        "platform": "Kubernetes",
        "hostname": socket.gethostname()
    }