# Security Policy

## Supported Versions

This is a learning repo, so support is intentionally simple.

| Version | Supported |
| --- | --- |
| `main` | Yes |
| older commits and branches | No |

Security fixes, scanner tuning, and dependency updates are only expected on `main`.

## Reporting a Vulnerability

Please do not open a public GitHub issue for a suspected security vulnerability.

Preferred reporting path:

1. Use GitHub private vulnerability reporting for this repository, if it is enabled.
2. If private reporting is not available, contact the repository owner privately before sharing details publicly.

Please include:

- a short description of the issue
- affected file or workflow
- reproduction steps
- impact
- any suggested fix or mitigation

## What To Expect

This repository is a personal learning project, not a production service.

- response times are best effort
- fixes may be educational rather than enterprise-grade
- some insecure patterns may exist intentionally to demonstrate scanner findings and pipeline behavior

## Scope

This policy covers:

- application code in `examples/`
- GitHub Actions workflows
- GitLab CI definitions
- Docker and Docker Compose files in examples
- Kubernetes manifests in `examples/*/k8s/`

It does not guarantee support for forks, old branches, or copied downstream uses.
