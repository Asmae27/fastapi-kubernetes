# FastAPI Application Deployment with Kubernetes

## Overview

This project demonstrates how to deploy a containerized **FastAPI application** on a local Kubernetes cluster using **Kind (Kubernetes in Docker)**.

The main objective is to understand the fundamentals of Kubernetes orchestration through a practical exercise, including application deployment, service exposure, horizontal scaling, and automatic Pod recovery.

## Objectives

- Build a REST API using FastAPI.
- Containerize the application using Docker.
- Create a local Kubernetes cluster using Kind.
- Deploy the application using a Kubernetes Deployment.
- Expose the application internally using a Kubernetes Service.
- Scale the application from 1 to 3 replicas.
- Test Kubernetes self-healing by deleting a Pod and observing its automatic replacement.

## Technologies

| Technology | Purpose |
|---|---|
| Python 3.12 | Application development |
| FastAPI | REST API framework |
| Uvicorn | ASGI application server |
| Docker | Application containerization |
| Kubernetes | Container orchestration |
| Kind | Local Kubernetes cluster |
| kubectl | Kubernetes command-line interface |

## Project Structure

```text
fastapi-kubernetes/
│
├── app/
│   └── main.py
│
├── kubernetes/
│   ├── deployment.yaml
│   └── service.yaml
│
├── Dockerfile
├── requirements.txt
└── README.md
```

## Application Endpoints

The FastAPI application exposes three endpoints:

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Returns a welcome message and Pod hostname |
| GET | `/health` | Checks application health |
| GET | `/info` | Returns application and platform information |

The hostname allows us to identify which Pod handled a request.

## Prerequisites

Make sure the following tools are installed:

- Docker Desktop
- Python 3.12+
- kubectl
- Kind

Verify the installations:

```bash
docker --version
kubectl version --client
python3 --version
kind version
```

## Installation and Deployment

### 1. Clone the repository

```bash
git clone https://github.com/Asmae27/fastapi-kubernetes.git
cd fastapi-kubernetes
```

### 2. Build the Docker image

```bash
docker build -t fastapi-k8s:v1 .
```

### 3. Create the Kind cluster

```bash
kind create cluster --name fastapi-cluster
```

Verify the cluster:

```bash
kubectl get nodes
```

### 4. Load the Docker image into Kind

```bash
kind load docker-image fastapi-k8s:v1 --name fastapi-cluster
```

This makes the locally built image available to the Kubernetes cluster.

### 5. Deploy the application

Apply the Deployment configuration:

```bash
kubectl apply -f kubernetes/deployment.yaml
```

Apply the Service configuration:

```bash
kubectl apply -f kubernetes/service.yaml
```

Check the deployed resources:

```bash
kubectl get deployments
kubectl get pods
kubectl get services
```

### 6. Access the application

Forward the Service port to your local machine:

```bash
kubectl port-forward service/fastapi-service 8080:80
```

Open the following URLs:

- [http://localhost:8080/](http://localhost:8080/)
- [http://localhost:8080/health](http://localhost:8080/health)
- [http://localhost:8080/info](http://localhost:8080/info)
- [http://localhost:8080/docs](http://localhost:8080/docs)

The Swagger UI at `/docs` allows you to interact with the API.

## Kubernetes Experiments

### Experiment 1: Horizontal Scaling

Initially, the Deployment runs one replica.

Scale the application to three replicas:

```bash
kubectl scale deployment fastapi-deployment --replicas=3
```

Check the Pods:

```bash
kubectl get pods
```

Expected result: three application Pods running in the cluster.

### Experiment 2: Automatic Pod Recovery

Kubernetes continuously monitors the desired state defined in the Deployment.

Delete one of the running Pods:

```bash
kubectl delete pod <POD_NAME>
```

Observe the Pods:

```bash
kubectl get pods -w
```

**Expected behavior:**

- Kubernetes detects that the number of available Pods is below the desired replica count.
- The ReplicaSet controller creates a replacement Pod.
- The Deployment returns to its desired state of three replicas.

This demonstrates Kubernetes' self-healing mechanism.

### Experiment 3: Inspect the Application Pods

Display detailed information about the Deployment:

```bash
kubectl describe deployment fastapi-deployment
```

Display the Service endpoints:

```bash
kubectl get endpointslices -l kubernetes.io/service-name=fastapi-service
```

These endpoints identify the Pods selected by the Service.

## Key Kubernetes Concepts Learned

| Concept | Role |
|---|---|
| Pod | Smallest deployable Kubernetes unit |
| Deployment | Manages application replicas and updates |
| ReplicaSet | Ensures the desired number of Pods exists |
| Service | Provides stable network access to Pods |
| Scaling | Changes the number of application replicas |
| Self-healing | Replaces failed or deleted Pods |
| Kind | Runs a local Kubernetes cluster using Docker |

## Cleanup

Delete the Kubernetes resources:

```bash
kubectl delete -f kubernetes/
```

Delete the local Kind cluster:

```bash
kind delete cluster --name fastapi-cluster
```

## Learning Outcomes

Through this project, I gained practical experience with:

- Docker image creation and containerization.
- Kubernetes cluster management.
- Declarative application deployment using YAML manifests.
- Service discovery and networking.
- Horizontal scaling and replica management.
- Kubernetes self-healing and reconciliation.

---

**Author:** Asmae Kheirati

**Project:** FastAPI Application Deployment with Kubernetes

**Context:** Kubernetes Practical Lab