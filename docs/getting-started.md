# Getting Started

This guide is the fastest way to get productive with the starter kit.

## Prerequisites

- Python 3.12 or compatible local Python 3.x
- Docker or Rancher Desktop
- `kubectl` if you want to try the Kubernetes path
- GitHub or GitLab if you want to exercise the CI workflows

## Start Here

If you only want one success path first, do this:

```bash
cd examples/python-flask
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Then open `http://localhost:5000`.

## Docker Path

```bash
cd examples/python-flask
docker compose up --build
```

Useful follow-up commands:

```bash
docker compose logs -f
docker compose exec web sh
docker compose exec db psql -U appuser -d appdb
docker compose down
```

## Kubernetes Path

Build the image:

```bash
docker build -t tiny-sdlc-app:dev examples/python-flask
```

Deploy the manifests:

```bash
kubectl apply -k examples/python-flask/k8s
kubectl get all -n tiny-sdlc-app
kubectl port-forward svc/tiny-sdlc-web 5000:5000 -n tiny-sdlc-app
```

## CI Path

If you want to learn the automation side next, read:

- [`ci/README.md`](../ci/README.md)
- [`ci/catalog.md`](../ci/catalog.md)
- [`ci/github/README.md`](../ci/github/README.md)
- [`ci/gitlab/README.md`](../ci/gitlab/README.md)

## Troubleshooting

### Python dependencies fail to install

- confirm your virtual environment is active
- confirm you are running the command from `examples/python-flask`
- if your corporate environment uses a custom package index, check access first

### Docker build fails

- confirm Docker or Rancher Desktop is running
- confirm your environment can pull the base image used by `examples/python-flask/Dockerfile`
- if Docker Hub access is restricted, use your approved registry mirror

### Kubernetes commands fail

- confirm `kubectl cluster-info` works first
- confirm your local cluster can see the image you built
- if it cannot, push the image to a registry and update the deployment image reference

### CI behaves differently by platform

- GitHub has richer security surfacing in this repository
- GitLab keeps the baseline validate, build, and core security scans
- `ci/catalog.md` shows which controls are shared and which are platform-specific
