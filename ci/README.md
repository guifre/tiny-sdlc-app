# CI Overview

This repository keeps platform-specific entrypoints where GitHub and GitLab expect them, but moves repeated command logic into shared scripts under `ci/scripts/`.

## Scan Catalog

- `validate`: install the example dependencies and verify Python syntax
- `build`: build the example Docker image
- `sast`: run Semgrep CE against the repository
- `secret-scan`: run Gitleaks and emit SARIF
- `iac-scan`: run Checkov against Kubernetes manifests in the repository
- `sca`: run OSV-Scanner against repository dependency manifests
- `sbom`: generate an SBOM and dependency snapshot
- `dast`: run an OWASP ZAP baseline scan against the running example app

## Layout

- `ci/scripts/`: shared shell scripts used by both GitHub Actions and GitLab CI where practical
- `ci/github/README.md`: how the GitHub workflows are organized
- `ci/gitlab/README.md`: how the GitLab pipeline is organized

## Reuse Pattern

If you adapt this starter kit:

1. keep the platform entrypoints in `.github/workflows/` and `.gitlab-ci.yml`
2. update `EXAMPLE_DIR` and image tags to match your app
3. keep the shared shell scripts thin and repo-specific
4. decide which scanners should be blocking versus informational
