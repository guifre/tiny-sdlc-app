# GitHub Actions Layout

The GitHub workflows are split by control area so each workflow maps to one kind of signal in the repository.

## Workflows

- `ci.yml`: validate the Python example and build its Docker image
- `semgrep.yml`: SAST with SARIF upload to GitHub code scanning
- `gitleaks.yml`: secret scanning with SARIF upload to GitHub code scanning
- `checkov.yml`: Kubernetes/IaC scanning with SARIF upload to GitHub code scanning
- `osv-scanner.yml`: dependency vulnerability scanning
- `sbom.yml`: SBOM generation and dependency snapshot submission
- `zap-baseline.yml`: non-blocking DAST with artifact reporting

## Shared Inputs

Workflows that operate on the example app use:

- `EXAMPLE_DIR=examples/python-flask`
- shared scripts from `ci/scripts/`

## Notes

- GitHub code scanning is used for SARIF-capable scanners.
- ZAP stays artifact-based because this setup is a lightweight baseline scan.
- OSV-Scanner and SBOM stay GitHub-native because they integrate well with GitHub security features.
