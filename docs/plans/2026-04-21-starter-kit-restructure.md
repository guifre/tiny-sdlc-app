# Starter Kit Repositioning Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Reposition the repository as a reusable secure SDLC starter kit, move the current Flask app into `examples/python-flask/`, and make GitHub and GitLab CI clearer and more reusable.

**Architecture:** Keep platform-required CI entrypoints in place, but move repeated command logic into shared shell scripts and document the repository around reusable capabilities. Treat the Flask app as a first example, not the repository itself.

**Tech Stack:** Python, Flask, Docker, Docker Compose, Kubernetes manifests, GitHub Actions, GitLab CI, Semgrep, Gitleaks, Checkov, OSV-Scanner, Syft, OWASP ZAP

---

### Task 1: Create the starter-kit support structure

**Files:**
- Create: `docs/plans/2026-04-21-starter-kit-restructure-design.md`
- Create: `docs/plans/2026-04-21-starter-kit-restructure.md`
- Create: `ci/README.md`
- Create: `ci/github/README.md`
- Create: `ci/gitlab/README.md`
- Create: `ci/scripts/*.sh`

**Step 1: Create the support directories and docs skeleton**

Create `ci/`, `ci/github/`, `ci/gitlab/`, and `ci/scripts/`.

**Step 2: Write the CI overview docs**

Document the scan categories, platform differences, and how shared scripts are used.

**Step 3: Add shared executable scripts**

Add scripts for:

- example validation
- example Docker build
- Semgrep
- Gitleaks
- Checkov

**Step 4: Mark scripts executable**

Use `chmod +x` on the script files.

### Task 2: Move the Flask app into the example directory

**Files:**
- Move: `app.py` to `examples/python-flask/app.py`
- Move: `requirements.txt` to `examples/python-flask/requirements.txt`
- Move: `Dockerfile` to `examples/python-flask/Dockerfile`
- Move: `docker-compose.yml` to `examples/python-flask/docker-compose.yml`
- Move: `start.sh` to `examples/python-flask/start.sh`
- Move: `k8s/` to `examples/python-flask/k8s/`
- Modify: `.gitignore`

**Step 1: Move the app files**

Preserve file contents while relocating them to `examples/python-flask/`.

**Step 2: Update ignore rules**

Change `.gitignore` so example-local artifacts like `app.db` and `__pycache__/` are still ignored from the new location.

**Step 3: Check for relative-path assumptions**

Verify Docker, Compose, and app path behavior still works from the new directory.

### Task 3: Update GitHub Actions for the new structure

**Files:**
- Modify: `.github/workflows/ci.yml`
- Modify: `.github/workflows/semgrep.yml`
- Modify: `.github/workflows/gitleaks.yml`
- Modify: `.github/workflows/checkov.yml`
- Modify: `.github/workflows/osv-scanner.yml` if path references are needed
- Modify: `.github/workflows/sbom.yml` if path references are needed
- Modify: `.github/workflows/zap-baseline.yml`

**Step 1: Introduce a shared example path**

Use an `EXAMPLE_DIR` environment variable where it improves readability.

**Step 2: Delegate repeated commands to shared scripts**

Call scripts from `ci/scripts/` for validation, Docker build, Semgrep, Gitleaks, and Checkov.

**Step 3: Update path-sensitive workflows**

Ensure ZAP runs the app from the new location and build steps use the new Docker context.

### Task 4: Update GitLab CI for the new structure

**Files:**
- Modify: `.gitlab-ci.yml`

**Step 1: Add shared variables**

Introduce the example directory as a single variable.

**Step 2: Reuse the same shell scripts**

Replace inline validation, build, Semgrep, Gitleaks, and Checkov commands with calls to `ci/scripts/`.

**Step 3: Improve section clarity**

Keep stages simple and grouped by validate, build, and security responsibilities.

### Task 5: Rewrite the README as a starter kit

**Files:**
- Modify: `README.md`

**Step 1: Replace app-first intro with template-first positioning**

Lead with what the repository gives you.

**Step 2: Add repository map**

Show where the example app, CI docs, threat model, and policies live.

**Step 3: Move example run instructions under an examples section**

Update all commands to use `examples/python-flask/`.

**Step 4: Add CI guidance**

Point readers to GitHub and GitLab docs under `ci/`.

### Task 6: Verify and prepare commit guidance

**Files:**
- Review all modified files

**Step 1: Run validation**

Run:

```bash
git status --short
bash ci/scripts/validate-python-example.sh
bash ci/scripts/build-python-example-image.sh
```

**Step 2: Spot-check the new layout**

Run:

```bash
find examples/python-flask -maxdepth 2 -type f | sort
```

**Step 3: Review CI files**

Open the GitHub workflow files and `.gitlab-ci.yml` to confirm they now point at the shared scripts and example path.

**Step 4: Commit**

```bash
git add README.md .gitignore .github/workflows .gitlab-ci.yml ci docs/plans examples/python-flask
git commit -m "refactor: reposition repo as starter kit"
```
