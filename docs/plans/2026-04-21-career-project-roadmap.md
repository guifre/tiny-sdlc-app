# Career Project Roadmap Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a sequence of hands-on security and platform projects that strengthens DevSecOps depth, enterprise credibility, and reusable consulting-style assets.

**Architecture:** Start from the current secure SDLC starter kit, then expand outward into cloud deployment, software supply chain security, AI security, and automation. Each project should become both a learning exercise and a reusable portfolio asset.

**Tech Stack:** GitHub Actions, GitLab CI, Docker, Kubernetes, Terraform, Semgrep, Gitleaks, Checkov, OSV-Scanner, Syft, Cosign, OWASP ZAP, Python, Flask, cloud services, OIDC, LLM tooling

---

## Priorities

### Phase 1: Strengthen the current starter kit

**Why this matters:**
- It compounds work already done.
- It is the fastest path to a polished portfolio project.
- It can evolve into a reusable consulting accelerator.

**Outcomes to aim for:**
- cleaner template onboarding
- reusable app replacement guide
- more polished CI documentation
- optional cloud-ready path

### Phase 2: Deploy one version to a real cloud

**Why this matters:**
- It closes the gap between local demos and real delivery.
- It gives stronger architecture and platform credibility.

**Outcomes to aim for:**
- Terraform-managed infrastructure
- managed database
- DNS and TLS
- secrets management
- IaC scanning in CI

### Phase 3: Add software supply chain security

**Why this matters:**
- This is highly relevant in enterprise work.
- It strengthens your story beyond basic CI scanning.

**Outcomes to aim for:**
- SBOM maturity
- image scanning
- image signing with `cosign`
- provenance or attestations
- admission or policy checks

### Phase 4: Build an AI/LLM security example

**Why this matters:**
- It adds a modern security angle.
- It is useful for both learning and marketability.

**Outcomes to aim for:**
- prompt injection scenarios
- unsafe tool use controls
- logging and redaction
- secret handling
- secure deployment patterns

### Phase 5: Turn the knowledge into automation

**Why this matters:**
- It shifts you from practitioner to productizer.
- It creates reusable internal and client-facing assets.

**Outcomes to aim for:**
- repo bootstrap CLI or GitHub App
- automatic CI and policy scaffolding
- starter threat model generation
- baseline secure repo configuration

## Suggested Project Sequence

### Project 1: Secure SDLC Starter Kit v2

**Scope:**
- improve template onboarding
- add "replace the example app" guidance
- add stronger reusable docs
- optionally add one more example later

**Why first:**
- highest leverage
- already in motion

### Project 2: Cloud Deployment Reference

**Scope:**
- deploy the example to one cloud
- manage infra with Terraform
- keep security scanning in the pipeline

**Why second:**
- adds real-world deployment depth

### Project 3: Supply Chain Security Lab

**Scope:**
- sign images
- attach SBOMs
- add provenance
- enforce image policy

**Why third:**
- very strong enterprise signal

### Project 4: AI Security Demo

**Scope:**
- small RAG or chatbot app
- abuse cases and mitigations
- CI/CD and deployment story

**Why fourth:**
- keeps your profile current

### Project 5: DevSecOps Bootstrap Tool

**Scope:**
- script or app that adds starter workflows and docs
- generate `SECURITY.md`, `CODEOWNERS`, and baseline pipelines

**Why fifth:**
- strongest bridge to a reusable offering

## Decision Filters

Use these questions before starting a new project:

1. Does it improve technical depth?
2. Does it look credible to enterprise teams?
3. Can it become a reusable asset?
4. Can you explain it clearly in a CV, interview, or client call?

If a project scores low on at least three of these, it is probably not the best next move.

## Near-Term Next Steps

### Task 1: Finish polishing the current starter kit

**Files:**
- Review: `README.md`
- Review: `ci/`
- Review: `examples/python-flask/`
- Review: `docs/threat-model.md`

**Step 1:**
Review the repo as if it were being published publicly.

**Step 2:**
List remaining gaps for template quality, docs, and automation.

**Step 3:**
Pick the next smallest improvement and implement it.

### Task 2: Define the cloud target

**Files:**
- Create later: `docs/plans/<cloud-deployment-plan>.md`

**Step 1:**
Choose one cloud to learn first.

**Step 2:**
Choose the runtime target: Kubernetes or simpler container hosting.

**Step 3:**
Write the cloud deployment plan before building.

### Task 3: Reserve a future slot for AI security

**Files:**
- Create later: `docs/plans/<ai-security-plan>.md`

**Step 1:**
Pick one concrete AI app shape.

**Step 2:**
List the top abuse cases to simulate.

**Step 3:**
Turn that into a hands-on repo plan.

## Notes

- The best immediate path is still: starter kit -> cloud deployment -> supply chain -> AI security -> automation.
- This roadmap is meant to be practical, portfolio-friendly, and reusable.
- Keep each project small enough to finish and polished enough to show.
