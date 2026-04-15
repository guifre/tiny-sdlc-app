# Tiny SDLC App

This is a deliberately small app for learning:

- app code
- database basics
- Docker image builds
- Docker Compose
- Kubernetes manifests
- CI security scans with Semgrep
- GitHub-native security workflows for code, secrets, and Kubernetes manifests
- Dependency update and vulnerability scanning with Dependabot and OSV-Scanner

## What it does

- `GET /` shows a tiny web page
- `POST /notes` adds a note
- `GET /api/notes` returns notes as JSON
- `GET /healthz` returns a health check

By default it uses SQLite, which keeps the first run simple.
Later we can set `DATABASE_URL` and move it to Postgres without changing app code.

## Run locally

```bash
cd /Users/guifruiz/Documents/docker-kubernetes/tiny-sdlc-app
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Then open `http://localhost:5000`.

## Run with Docker Compose

Install Docker Desktop first. Then from this directory run:

```bash
cd /Users/guifruiz/Documents/docker-kubernetes/tiny-sdlc-app
docker compose up --build
```

Then open:

- `http://localhost:5000`
- `http://localhost:5000/healthz`
- `http://localhost:5000/api/notes`

This starts:

- `web`: the Flask app in a Python container
- `db`: PostgreSQL 16

The app container waits for the database and then creates the `notes` table on startup.

## What To Learn While Running It

1. Inspect running containers with `docker ps`
2. Read logs with `docker compose logs -f`
3. Enter the app container with `docker compose exec web sh`
4. Enter Postgres with `docker compose exec db psql -U appuser -d appdb`
5. Stop the stack with `docker compose down`
6. Remove the database volume with `docker compose down -v`

## Files Added For Containerization

- `Dockerfile`: builds the app image
- `start.sh`: waits for database setup, then starts Gunicorn
- `docker-compose.yml`: runs the app and Postgres together
- `.dockerignore`: keeps local clutter out of the image

## Run with Kubernetes

This repo includes plain manifests in `k8s/` so you can learn the basics before using Helm.

Why this stage matters for the original goal:

- today, you are running one app and one database
- later, the same Kubernetes ideas apply to CI runners, Semgrep jobs, and security tooling
- this stage is about learning how Kubernetes keeps workloads alive, exposes them, scales them, updates them, and helps you debug them

Build the app image first:

```bash
cd /Users/guifruiz/Documents/docker-kubernetes/tiny-sdlc-app
docker build -t tiny-sdlc-app:dev .
```

Make sure your local Kubernetes cluster is running first:

```bash
kubectl cluster-info
```

If your Kubernetes cluster cannot see local images, push the image to your registry and update `k8s/web-deployment.yaml`.

Apply the manifests:

```bash
kubectl apply -k k8s
kubectl get all -n tiny-sdlc-app
kubectl get pvc -n tiny-sdlc-app
```

Check rollout status:

```bash
kubectl rollout status deployment/postgres -n tiny-sdlc-app
kubectl rollout status deployment/tiny-sdlc-web -n tiny-sdlc-app
```

Access the app locally:

```bash
kubectl port-forward svc/tiny-sdlc-web 5000:5000 -n tiny-sdlc-app
```

Then open:

- `http://localhost:5000`
- `http://localhost:5000/healthz`
- `http://localhost:5000/api/notes`

Useful debugging commands:

```bash
kubectl get pods -n tiny-sdlc-app
kubectl logs deployment/tiny-sdlc-web -n tiny-sdlc-app
kubectl logs deployment/postgres -n tiny-sdlc-app
kubectl exec -it deployment/tiny-sdlc-web -n tiny-sdlc-app -- sh
kubectl exec -it deployment/postgres -n tiny-sdlc-app -- psql -U appuser -d appdb
kubectl delete -k k8s
```

What these manifests teach:

- `Namespace`: logical isolation
- `Secret`: database credentials and connection string
- `ConfigMap`: non-secret app settings
- `Deployment`: desired state for app and database pods
- `Service`: stable DNS name inside the cluster
- `PersistentVolumeClaim`: database storage

## Stage 2 Tutorial: Deploy, Expose, Scale, Update, Debug

This section is the hands-on Kubernetes stage for this project.

Your mental model:

- Docker built the image
- Kubernetes runs that image as a pod
- a `Deployment` keeps the pod alive
- a `Service` gives the app a stable network name
- `kubectl` is the main command-line tool for talking to the cluster

### 1. Deploy

Build the app image so the cluster has something to run:

```bash
docker build -t tiny-sdlc-app:dev .
```

Why:

- this turns your app source code into a runnable container image
- your web deployment is configured to use `tiny-sdlc-app:dev`

Apply all Kubernetes manifests:

```bash
kubectl apply -k k8s
```

Why:

- `apply` means create or update resources
- `-k k8s` means load everything from the `k8s/kustomization.yaml` bundle
- this creates the namespace, config, secrets, database, web app, services, and storage

Check what got created:

```bash
kubectl get all -n tiny-sdlc-app
kubectl get pvc -n tiny-sdlc-app
```

Why:

- `get all` gives you the main app resources: pods, services, deployments, replicasets
- `get pvc` confirms the database storage claim exists

Wait until Kubernetes says the app is healthy:

```bash
kubectl rollout status deployment/postgres -n tiny-sdlc-app
kubectl rollout status deployment/tiny-sdlc-web -n tiny-sdlc-app
```

Why:

- Kubernetes may need time to pull images, create pods, and pass health checks
- Postgres needs to be ready before the app can talk to the database

### 2. Expose

Expose the app to your laptop:

```bash
kubectl port-forward svc/tiny-sdlc-web 5000:5000 -n tiny-sdlc-app
```

Why:

- the app is running inside the cluster, not directly on your laptop
- `port-forward` creates a temporary tunnel from your machine to the Kubernetes `Service`
- after this, `http://localhost:5000` reaches the app in the cluster

Check the endpoints:

```bash
curl http://127.0.0.1:5000/healthz
curl http://127.0.0.1:5000/api/notes
```

Why:

- `/healthz` confirms the app and database are reachable
- `/api/notes` confirms the app is serving requests inside Kubernetes

### 3. Scale

Increase the number of web app replicas:

```bash
kubectl scale deployment/tiny-sdlc-web --replicas=2 -n tiny-sdlc-app
kubectl get pods -n tiny-sdlc-app -l app=tiny-sdlc-web
```

Why:

- this is one of Kubernetes' core jobs: keep multiple copies of your app running
- the `Service` load-balances traffic across matching pods
- this is the same pattern used later for scalable internal platforms and CI workers

Scale back down:

```bash
kubectl scale deployment/tiny-sdlc-web --replicas=1 -n tiny-sdlc-app
```

### 4. Update

You have two common ways to update in this tutorial:

1. Rebuild a local image and restart the deployment
2. Point the deployment at a different tag

Rebuild and restart:

```bash
docker build -t tiny-sdlc-app:dev .
kubectl rollout restart deployment/tiny-sdlc-web -n tiny-sdlc-app
kubectl rollout status deployment/tiny-sdlc-web -n tiny-sdlc-app
```

Why:

- rebuilding updates the image contents
- restarting the deployment makes Kubernetes replace old pods with new ones

Or update the image tag directly:

```bash
kubectl set image deployment/tiny-sdlc-web web=tiny-sdlc-app:dev -n tiny-sdlc-app
kubectl rollout status deployment/tiny-sdlc-web -n tiny-sdlc-app
```

Why:

- this is closer to how CI/CD works later
- in a real pipeline, GitHub Actions would build a new image tag and Kubernetes would roll out that tag

### 5. Debug

When something breaks, start with these:

```bash
kubectl get pods -n tiny-sdlc-app
kubectl describe pod -n tiny-sdlc-app -l app=tiny-sdlc-web
kubectl logs deployment/tiny-sdlc-web -n tiny-sdlc-app
kubectl logs deployment/postgres -n tiny-sdlc-app
kubectl exec -it deployment/tiny-sdlc-web -n tiny-sdlc-app -- sh
kubectl exec -it deployment/postgres -n tiny-sdlc-app -- psql -U appuser -d appdb
```

What each one helps with:

- `get pods`: quick status like `Running`, `Pending`, `CrashLoopBackOff`, `ImagePullBackOff`
- `describe pod`: detailed events such as image pull failures, probe failures, scheduling issues
- `logs`: app or database output
- `exec`: open a shell inside the running container

Examples of real problems from this project:

- `ImagePullBackOff`: Kubernetes could not find or pull the image
- rollout timeout: the pod started but did not become ready in time
- `port-forward` failure: the service had no healthy backing pod yet

### 6. Clean Up

Delete everything when you want a fresh start:

```bash
kubectl delete -k k8s
```

Why:

- this removes the namespace resources for this lab
- it is the Kubernetes equivalent of tearing down your Compose stack

### 7. What You Should Learn From This Stage

By the end of this stage, you should be comfortable with:

- deploying an app to a local cluster
- exposing it to your laptop
- scaling replicas up and down
- updating the running version
- using logs, describe, and exec to debug problems

That is the foundation you need before adding:

- GitHub Actions jobs that build images
- Semgrep scans that run in pipelines
- Gitleaks secret scanning
- Checkov Kubernetes manifest scanning
- Dependabot dependency and GitHub Actions updates
- OSV-Scanner dependency vulnerability scanning
- DefectDojo or other security platforms that collect and display results

## Stage 3 Preview: GitHub Actions

For the next stage, this project uses GitHub Actions instead of GitLab CI.

Why:

- it is simpler for a personal learning repo
- it keeps the focus on CI concepts instead of GitLab administration
- it still teaches the same core flow: code change -> automated checks -> image build -> later security scan

The main CI workflow file lives here:

- `.github/workflows/ci.yml`

What it does:

- checks out the repository
- installs Python dependencies
- verifies `app.py` syntax
- builds the Docker image in CI

This is the GitHub equivalent of your first CI pipeline step.

Security workflows in this repo:

- `.github/workflows/semgrep.yml`
- `.github/workflows/gitleaks.yml`
- `.github/workflows/checkov.yml`
- `.github/workflows/osv-scanner.yml`
- `.github/dependabot.yml`

What they do:

- `semgrep.yml`
  scans the Python app, Dockerfile, and Kubernetes YAML with Semgrep CE
  uploads SARIF as an artifact
  uploads findings to GitHub code scanning

- `gitleaks.yml`
  scans the repository for committed secrets
  uploads SARIF as an artifact
  uploads findings to GitHub code scanning
  does not fail the workflow by default

- `checkov.yml`
  scans the Kubernetes manifests in `k8s/`
  uploads SARIF as an artifact
  uploads findings to GitHub code scanning
  does not fail the workflow by default

- `osv-scanner.yml`
  scans the repository for dependency vulnerabilities
  uploads SARIF to GitHub code scanning
  runs on pushes to `main`, weekly on a schedule, and on demand
  does not fail the workflow by default

- `dependabot.yml`
  checks for Python dependency updates
  checks for GitHub Actions version updates

Why keep it separate at first:

- it is easier to understand than mixing build and security checks together
- you can learn the normal CI workflow and the security scan workflow independently

Later, you can extend it with:

- more specific Semgrep rule selection
- tighter Checkov policy selection and suppressions
- OSV-Scanner tuning for dependency scope and policy
- image push to a registry
- deployment automation

## Next steps

1. Run the stack in Docker Compose
2. Run the stack in Kubernetes
3. Review findings in GitHub code scanning
4. Tune Semgrep rules and scanner scope
5. Tune Checkov scope for the Kubernetes manifests
6. Review OSV-Scanner dependency findings
7. Add another security layer such as DefectDojo or SBOM generation
