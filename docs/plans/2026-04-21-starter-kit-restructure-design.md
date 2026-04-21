# Starter Kit Repositioning Design

## Summary

Reposition the repository from a single tutorial app into a reusable secure SDLC starter kit. The repository root should explain the reusable capabilities, while the existing Flask app becomes a concrete example implementation under `examples/python-flask/`.

## Goals

- Make the repository read like a starter kit/template instead of a one-off demo.
- Preserve the current learning flow: app, Docker, Kubernetes, GitHub CI, GitLab CI, and security tooling.
- Keep a runnable reference example for hands-on learning.
- Make CI easier to understand by grouping platform-specific workflows around shared concepts and shared scripts.

## Non-Goals

- Expanding the number of example applications.
- Changing the app's behavior or fixing current scan findings.
- Introducing a release process, packaging system, or product tiering.

## Proposed Structure

- Root-level docs and metadata stay at the root:
  - `README.md`
  - `SECURITY.md`
  - `.github/`
  - `.gitlab-ci.yml`
  - `docs/`
- The current app moves to:
  - `examples/python-flask/`
- New CI support docs and shared scripts live under:
  - `ci/`
  - `ci/scripts/`
  - `ci/github/`
  - `ci/gitlab/`

## Example App Design

The Flask example remains intentionally small and insecure-by-design in a few places so the scanners still have something meaningful to find. The move to `examples/python-flask/` should be path-only: no functional behavior change unless needed to keep relative paths working.

Assets that move with the example:

- `app.py`
- `requirements.txt`
- `Dockerfile`
- `docker-compose.yml`
- `start.sh`
- `k8s/`

## CI Design

Platform-required entrypoints stay where the platforms expect them:

- GitHub workflows remain in `.github/workflows/`
- GitLab pipeline remains in `.gitlab-ci.yml`

To make them clearer and more reusable:

- Add shared shell scripts in `ci/scripts/` for repeated repository tasks such as Python validation, Docker build, Semgrep, Gitleaks, and Checkov.
- Keep workflows thin by delegating repeated command logic to those scripts.
- Add concise platform docs under `ci/github/README.md` and `ci/gitlab/README.md`.
- Introduce root-level path variables in workflows/pipelines so the example location is explicit.

## Documentation Design

The new root README should:

- Lead with the starter-kit positioning.
- Show what the repository includes.
- Explain where the example app lives.
- Separate "use the template" from "run the example".
- Point readers to GitHub/GitLab CI docs and the threat model.

The existing app-specific operational steps should move into the example section of the README, with commands updated for the new path.

## Risks

- Path regressions in CI after moving the app.
- Broken Docker and Kubernetes commands if contexts are not updated carefully.
- Docs drift if commands still reference the old root-level layout.

## Validation

- Run the example validation script locally.
- Build the example Docker image locally.
- Confirm GitHub workflow YAML still parses and points at the new example path.
- Confirm `.gitlab-ci.yml` uses the same shared scripts and paths.
- Review `README.md` for a template-first narrative.
