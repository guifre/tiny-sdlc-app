# Secure SDLC Starter Kit

This repository is a small starter kit for learning and reusing secure delivery building blocks.

It combines:

- a tiny runnable example app
- Docker and Docker Compose
- Kubernetes manifests
- GitHub Actions security workflows
- a baseline GitLab CI pipeline
- threat modeling and repository security policy docs

The current reference app lives in `examples/python-flask/`, but the repository is intentionally structured so you can adapt it to a different app later.

## Start Here

If you want the fastest path to understanding the repo:

1. read [docs/getting-started.md](docs/getting-started.md)
2. run the Python Flask example once
3. skim [ci/catalog.md](ci/catalog.md)
4. read [docs/replace-the-example.md](docs/replace-the-example.md) before adapting it

If you only want one first success, run the local Python path from [docs/getting-started.md](docs/getting-started.md).

## What This Repo Gives You

- a concrete Python Flask example you can run locally, containerize, and deploy
- starter CI patterns for validation, SAST, secret scanning, IaC scanning, SCA, SBOM, and DAST
- GitHub-native code scanning integration for SARIF-capable tools
- a matching GitLab CI baseline for validate, build, Semgrep, Gitleaks, and Checkov
- documentation you can keep when generalizing the repository for your own projects

## Repository Map

| Path | Purpose |
| --- | --- |
| `examples/python-flask/` | runnable reference app, Docker assets, and Kubernetes manifests |
| `.github/workflows/` | GitHub Actions entrypoints |
| `.gitlab-ci.yml` | GitLab CI entrypoint |
| `ci/scripts/` | shared shell scripts reused by GitHub and GitLab jobs |
| `ci/github/` | GitHub workflow overview |
| `ci/gitlab/` | GitLab pipeline overview |
| `docs/threat-model.md` | repo and pipeline threat model |
| `SECURITY.md` | repository security reporting policy |

## How To Use It

You can use this repository in two ways:

1. learn by running the existing example app and security workflows
2. adapt the structure for another app while keeping the same CI and security building blocks

Suggested order:

1. run the example locally
2. run it with Docker Compose
3. deploy it to local Kubernetes
4. inspect the GitHub and GitLab CI layouts
5. replace the example app once the repo structure makes sense

Helpful companion docs:

- [Getting Started](docs/getting-started.md)
- [Replace The Example](docs/replace-the-example.md)
- [CI Catalog](ci/catalog.md)
- [Cloud Readiness](docs/cloud-readiness.md)

## Run The Current Example

### Local Python

```bash
cd examples/python-flask
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open `http://localhost:5000`.

### Docker Compose

```bash
cd examples/python-flask
docker compose up --build
```

Useful commands:

```bash
docker compose logs -f
docker compose exec web sh
docker compose exec db psql -U appuser -d appdb
docker compose down
docker compose down -v
```

### Local Kubernetes

Build the image:

```bash
docker build -t tiny-sdlc-app:dev examples/python-flask
```

Check the cluster:

```bash
kubectl cluster-info
```

Deploy the example:

```bash
kubectl apply -k examples/python-flask/k8s
kubectl get all -n tiny-sdlc-app
kubectl get pvc -n tiny-sdlc-app
kubectl rollout status deployment/postgres -n tiny-sdlc-app
kubectl rollout status deployment/tiny-sdlc-web -n tiny-sdlc-app
kubectl port-forward svc/tiny-sdlc-web 5000:5000 -n tiny-sdlc-app
```

Useful debug commands:

```bash
kubectl get pods -n tiny-sdlc-app
kubectl logs deployment/tiny-sdlc-web -n tiny-sdlc-app
kubectl logs deployment/postgres -n tiny-sdlc-app
kubectl exec -it deployment/tiny-sdlc-web -n tiny-sdlc-app -- sh
kubectl exec -it deployment/postgres -n tiny-sdlc-app -- psql -U appuser -d appdb
kubectl scale deployment/tiny-sdlc-web --replicas=2 -n tiny-sdlc-app
kubectl rollout restart deployment/tiny-sdlc-web -n tiny-sdlc-app
kubectl delete -k examples/python-flask/k8s
```

## CI And Security Automation

### GitHub

GitHub is the more complete integration in this repository today. It includes:

- CI validation and Docker build
- Semgrep with SARIF upload to the Security tab
- Gitleaks with SARIF upload to the Security tab
- Checkov with SARIF upload to the Security tab
- OSV-Scanner
- SBOM generation and dependency snapshot submission
- ZAP baseline as a non-blocking artifact-driven DAST check
- Dependabot for Python dependencies and GitHub Actions

See:

- [CI Overview](ci/README.md)
- [GitHub CI](ci/github/README.md)
- [CI Catalog](ci/catalog.md)

### GitLab

GitLab currently mirrors the baseline flow:

- validate
- build
- Semgrep
- Gitleaks
- Checkov

It is useful when you want equivalent pipeline structure in a GitLab-hosted project, even if the richer security surfacing in this repository stays GitHub-native.

See:

- [GitLab CI](ci/gitlab/README.md)
- `.gitlab-ci.yml`
- [CI Catalog](ci/catalog.md)

## Security Notes

- Some findings are intentionally left in place so the scanners have something to report.
- This is a starter kit and learning repo, not a production service.
- If you generalize it for real projects, tighten branch protection, action pinning, secrets handling, and environment-specific controls.
- If you want to evolve it toward real deployment, start with [docs/cloud-readiness.md](docs/cloud-readiness.md).

## Related Docs

- [Python Flask Example](examples/python-flask/README.md)
- [Threat Model](docs/threat-model.md)
- [Security Policy](SECURITY.md)
- [Getting Started](docs/getting-started.md)
- [Replace The Example](docs/replace-the-example.md)
- [Cloud Readiness](docs/cloud-readiness.md)
- [CI Catalog](ci/catalog.md)
