# Starter Kit V2 Phase 1 Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Improve the starter kit so it is easier to adopt, easier to adapt to another app, clearer in CI structure, and ready for a later cloud deployment track.

**Architecture:** Keep the current repository shape, then add missing onboarding and adaptation docs, tighten the CI documentation around reusable building blocks, and introduce lightweight cloud-readiness artifacts without adding cloud-specific code yet. This phase should improve clarity and reuse without expanding the app surface area much.

**Tech Stack:** Markdown docs, GitHub Actions, GitLab CI, Docker, Docker Compose, Kubernetes, Python Flask

---

### Task 1: Audit the current starter-kit experience

**Files:**
- Review: `/Users/guifruiz/Documents/docker-kubernetes/tiny-sdlc-app/README.md`
- Review: `/Users/guifruiz/Documents/docker-kubernetes/tiny-sdlc-app/ci/README.md`
- Review: `/Users/guifruiz/Documents/docker-kubernetes/tiny-sdlc-app/ci/github/README.md`
- Review: `/Users/guifruiz/Documents/docker-kubernetes/tiny-sdlc-app/ci/gitlab/README.md`
- Review: `/Users/guifruiz/Documents/docker-kubernetes/tiny-sdlc-app/examples/python-flask/README.md`
- Review: `/Users/guifruiz/Documents/docker-kubernetes/tiny-sdlc-app/docs/threat-model.md`

**Step 1: Review the repository as a first-time visitor**

Read the current top-level docs and note where adoption questions are still unanswered.

**Step 2: Write a gap list**

Create a short checklist of missing items for:
- onboarding
- app replacement
- CI reuse
- cloud readiness

**Step 3: Save the gap list**

Create:
- `/Users/guifruiz/Documents/docker-kubernetes/tiny-sdlc-app/docs/plans/2026-04-21-starter-kit-v2-gap-list.md`

### Task 2: Add stronger onboarding documentation

**Files:**
- Modify: `/Users/guifruiz/Documents/docker-kubernetes/tiny-sdlc-app/README.md`
- Create: `/Users/guifruiz/Documents/docker-kubernetes/tiny-sdlc-app/docs/getting-started.md`
- Modify: `/Users/guifruiz/Documents/docker-kubernetes/tiny-sdlc-app/examples/python-flask/README.md`

**Step 1: Draft a faster-start path**

Add a "Start Here" path in the root README with:
- what this repo is for
- the quickest successful run
- the next recommended learning steps

**Step 2: Write a dedicated getting-started doc**

Create `docs/getting-started.md` with:
- prerequisites
- local run path
- Docker path
- Kubernetes path
- where to look when something fails

**Step 3: Simplify the example README**

Keep the example README focused on the example itself and link back to the root docs for broader orientation.

**Step 4: Verify references**

Run:

```bash
rg -n "getting-started|Start Here|examples/python-flask" README.md docs examples/python-flask
```

Expected:
- new onboarding paths are discoverable from both the root README and the example README

### Task 3: Add a replace-the-example guide

**Files:**
- Create: `/Users/guifruiz/Documents/docker-kubernetes/tiny-sdlc-app/docs/replace-the-example.md`
- Modify: `/Users/guifruiz/Documents/docker-kubernetes/tiny-sdlc-app/README.md`
- Modify: `/Users/guifruiz/Documents/docker-kubernetes/tiny-sdlc-app/ci/README.md`

**Step 1: Define what is coupled to the current example**

List the files and concepts that assume `examples/python-flask/`, such as:
- Docker build context
- Python dependency install path
- Kubernetes manifests
- CI script variables

**Step 2: Document the swap process**

Write a guide that explains:
- what to replace
- what can stay
- which workflows need path updates
- how to validate the new example after replacement

**Step 3: Link the guide from the root**

Add links from the root README and `ci/README.md`.

**Step 4: Add a validation checklist**

Include exact commands such as:

```bash
sh ci/scripts/validate-python-example.sh
sh ci/scripts/build-python-example-image.sh
kubectl apply -k examples/python-flask/k8s
```

Expected:
- readers can see how to swap the example without reverse-engineering the repo

### Task 4: Clarify CI reuse and ownership

**Files:**
- Modify: `/Users/guifruiz/Documents/docker-kubernetes/tiny-sdlc-app/ci/README.md`
- Modify: `/Users/guifruiz/Documents/docker-kubernetes/tiny-sdlc-app/ci/github/README.md`
- Modify: `/Users/guifruiz/Documents/docker-kubernetes/tiny-sdlc-app/ci/gitlab/README.md`
- Create: `/Users/guifruiz/Documents/docker-kubernetes/tiny-sdlc-app/ci/catalog.md`
- Modify: `/Users/guifruiz/Documents/docker-kubernetes/tiny-sdlc-app/.github/workflows/ci.yml`
- Modify: `/Users/guifruiz/Documents/docker-kubernetes/tiny-sdlc-app/.gitlab-ci.yml`

**Step 1: Create a CI catalog**

Write `ci/catalog.md` to map each workflow/pipeline job to:
- purpose
- blocking vs non-blocking behavior
- output type
- platform support

**Step 2: Tighten the platform docs**

Make the GitHub and GitLab docs explicitly explain:
- what is shared
- what is platform-specific
- what would change for a new example

**Step 3: Consider small naming cleanup**

If useful, rename jobs or step titles in the workflow files so they read more consistently with the starter-kit positioning.

**Step 4: Verify CI discoverability**

Run:

```bash
rg -n "blocking|non-blocking|platform-specific|shared" ci .github/workflows .gitlab-ci.yml
```

Expected:
- CI behavior is easier to understand without opening every workflow in detail

### Task 5: Add cloud-ready preparation docs

**Files:**
- Create: `/Users/guifruiz/Documents/docker-kubernetes/tiny-sdlc-app/docs/cloud-readiness.md`
- Modify: `/Users/guifruiz/Documents/docker-kubernetes/tiny-sdlc-app/README.md`
- Modify: `/Users/guifruiz/Documents/docker-kubernetes/tiny-sdlc-app/docs/threat-model.md`

**Step 1: Define what "cloud-ready" means in this repo**

Document a lightweight readiness checklist covering:
- config separation
- secrets handling
- image publishing
- environment overlays
- DNS/TLS
- managed database migration
- IaC ownership

**Step 2: Connect it to the threat model**

Add a short section in the threat model about gaps that matter once the repo moves from local learning to cloud deployment.

**Step 3: Link it from the root README**

Make the future cloud track visible without pretending it is already implemented.

### Task 6: Verify the documentation pass

**Files:**
- Review all updated docs and CI files

**Step 1: Check changed files**

Run:

```bash
git status --short
```

Expected:
- only the intended Phase 1 docs and small workflow/doc cleanup changes are present

**Step 2: Validate internal references**

Run:

```bash
rg -n "replace-the-example|getting-started|cloud-readiness|ci/catalog" README.md docs ci examples
```

Expected:
- new docs are linked from the right places

**Step 3: Re-run example validation**

Run:

```bash
sh ci/scripts/validate-python-example.sh
```

Expected:
- the example still validates after the documentation and minor CI changes

**Step 4: Commit**

```bash
git add README.md docs ci examples/python-flask .github/workflows/ci.yml .gitlab-ci.yml
git commit -m "docs: improve starter kit onboarding"
```
