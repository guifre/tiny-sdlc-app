# Cloud Readiness

This repository is not deployed to a real cloud yet, but it can be prepared for that move without overbuilding too early.

## What Cloud-Ready Means Here

For this starter kit, "cloud-ready" means the repository can grow from local learning into a real environment with clear boundaries between:

- local-only behavior
- deployable application artifacts
- environment-specific configuration
- infrastructure ownership
- security controls that belong in CI versus runtime

## Readiness Checklist

### Configuration

- keep environment-specific values out of code
- separate local defaults from deploy-time configuration
- document required environment variables per example

### Secrets

- avoid hardcoded credentials in example manifests outside of training-only placeholders
- define where cloud secrets would live
- document secret ownership and rotation expectations

### Images And Registry

- define a real image naming convention
- document the target registry
- separate local image tags from deployable image tags

### Infrastructure

- decide whether Terraform will own networking, runtime, database, and DNS
- keep application manifests distinct from cloud infrastructure definitions
- plan for environment overlays such as `dev`, `stage`, and `prod`

### Runtime Hardening

- review Kubernetes security context findings intentionally left for training
- document what should change before any real deployment
- define where admission or policy checks would sit later

### Delivery

- define which CI jobs are required before deployment
- decide how image publishing, signing, and promotion will work
- decide whether GitHub, GitLab, or both remain part of the delivery story

## What Is Still Missing Today

- no Terraform or cloud infrastructure code
- no managed database path
- no registry publishing workflow
- no environment overlays
- no deployment promotion flow
- no cloud secrets integration

## Good Next Step

When you are ready for the next phase, write a cloud deployment plan that answers:

1. which cloud you want to learn first
2. whether you want Kubernetes or a simpler container runtime
3. what should stay reusable versus cloud-specific

That will keep the starter kit clean while still letting it evolve into a real delivery reference.
