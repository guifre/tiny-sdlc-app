# Python Flask Example

This example is the original tiny SDLC app from the repository. It stays intentionally small so you can practice:

- local Python runs
- Docker image builds
- Docker Compose
- Kubernetes basics
- CI security scanning

If you are new to the repository, start with:

- [`README.md`](../../README.md) for the starter-kit overview
- [`docs/getting-started.md`](../../docs/getting-started.md) for the fastest path
- [`docs/replace-the-example.md`](../../docs/replace-the-example.md) if you want to adapt this repo to another app

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

Then inspect:

```bash
docker compose logs -f
```

## Run with Kubernetes

```bash
docker build -t tiny-sdlc-app:dev examples/python-flask
kubectl apply -k examples/python-flask/k8s
kubectl get all -n tiny-sdlc-app
kubectl port-forward svc/tiny-sdlc-web 5000:5000 -n tiny-sdlc-app
```

This example is meant to stay small. The reusable repo-level guidance lives outside this folder on purpose.
