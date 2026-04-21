# Python Flask Example

This example is the original tiny SDLC app from the repository. It stays intentionally small so you can practice:

- local Python runs
- Docker image builds
- Docker Compose
- Kubernetes basics
- CI security scanning

## Run locally

```bash
cd examples/python-flask
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open `http://localhost:5000`.

## Run with Docker Compose

```bash
cd examples/python-flask
docker compose up --build
```

## Run with Kubernetes

```bash
docker build -t tiny-sdlc-app:dev examples/python-flask
kubectl apply -k examples/python-flask/k8s
kubectl get all -n tiny-sdlc-app
kubectl port-forward svc/tiny-sdlc-web 5000:5000 -n tiny-sdlc-app
```
