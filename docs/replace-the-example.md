# Replace The Example

This repository is structured so you can swap `examples/python-flask/` for your own app without throwing away the surrounding starter-kit pieces.

## What Is Coupled To The Current Example

These places currently assume `examples/python-flask/`:

- the root README commands
- `docs/getting-started.md`
- `examples/python-flask/README.md`
- `ci/scripts/common.sh` through `EXAMPLE_DIR`
- `.github/workflows/ci.yml`
- `.github/workflows/sbom.yml`
- `.github/workflows/zap-baseline.yml`
- `.github/dependabot.yml`
- `.gitlab-ci.yml`

These are mostly reusable and can often stay:

- `SECURITY.md`
- `.github/CODEOWNERS`
- secret scanning structure
- Semgrep workflow structure
- Checkov workflow structure
- CI documentation under `ci/`
- the threat model format

## Replacement Strategy

### Option 1: Replace In Place

Keep the path `examples/python-flask/` for your new app and swap the contents.

Why this is easiest:

- fewer path changes
- CI keeps working with minimal edits
- the starter-kit docs need less rewriting

### Option 2: Add A New Example Path

Create something like `examples/node-express/` or `examples/fastapi/`.

Why you might choose this:

- you want to keep the Flask example
- you plan to grow the repository into multiple examples

Tradeoff:

- more docs and CI updates
- you need to decide which example is the default one for validation and build jobs

## What To Update

### App Runtime

Update:

- app code and dependencies
- `Dockerfile`
- `docker-compose.yml`
- local run instructions

### Kubernetes

Update:

- manifests under your example's `k8s/`
- image name references
- config and secret values
- readiness and liveness probes

### CI Variables And Paths

Update:

- `EXAMPLE_DIR` in `ci/scripts/common.sh` if the default example changes
- `EXAMPLE_DIR` in `.github/workflows/ci.yml`
- `EXAMPLE_DIR` in `.github/workflows/semgrep.yml` if you want it to stay explicit
- `EXAMPLE_DIR` in `.github/workflows/zap-baseline.yml`
- `EXAMPLE_DIR` in `.gitlab-ci.yml`
- `.github/dependabot.yml` if dependency manifests move
- SBOM path in `.github/workflows/sbom.yml`

## Validation Checklist After Replacement

Run these from the repository root:

```bash
sh ci/scripts/validate-python-example.sh
sh ci/scripts/build-python-example-image.sh
kubectl apply -k examples/python-flask/k8s
```

If you changed the example path, update `EXAMPLE_DIR` first or create a matching new validation script.

Then also review:

- `README.md`
- `docs/getting-started.md`
- `ci/catalog.md`
- `docs/threat-model.md`

## Recommendation

For your next iteration, prefer replacing in place until you have a clear second example worth keeping. That keeps the starter kit simpler and makes the CI easier to reason about.
