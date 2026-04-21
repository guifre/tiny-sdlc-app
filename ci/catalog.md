# CI Catalog

| Control | GitHub | GitLab | Blocking | Output | Shared Parts | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Validate example | Yes | Yes | Yes | job result | `ci/scripts/validate-python-example.sh` | Installs example dependencies and checks Python syntax. |
| Build example image | Yes | Yes | Yes | job result | `ci/scripts/build-python-example-image.sh` | Uses the current default example Docker context. |
| Semgrep SAST | Yes | Yes | No | SARIF artifact; GitHub code scanning on GitHub | `ci/scripts/run-semgrep.sh` | GitHub uploads to the Security tab. |
| Gitleaks secret scan | Yes | Yes | No | SARIF artifact; GitHub code scanning on GitHub | workflow pattern plus `ci/scripts/run-gitleaks.sh` for GitLab | GitHub uses the existing action integration. |
| Checkov IaC scan | Yes | Yes | No | SARIF artifact; GitHub code scanning on GitHub | workflow pattern plus `ci/scripts/run-checkov.sh` for GitLab | GitHub uses the existing action integration. |
| OSV dependency scan | Yes | No | No | SARIF / GitHub-native results | none | Currently GitHub-specific in this starter kit. |
| SBOM generation | Yes | No | No | SPDX artifact and dependency snapshot | none | Currently GitHub-specific in this starter kit. |
| ZAP baseline DAST | Yes | No | No | HTML/report artifact | none | Lightweight GitHub-only baseline at the moment. |

## Shared Versus Platform-Specific

Shared today:

- example validation
- example Docker build
- Semgrep
- Gitleaks
- Checkov

Platform-specific today:

- GitHub code scanning upload
- OSV-Scanner
- SBOM snapshot submission
- ZAP baseline workflow

## Default Behavior

- GitHub uses a richer security reporting model.
- GitLab keeps a practical baseline pipeline.
- Secret, SAST, and IaC scanning are informational in this starter kit by default.
