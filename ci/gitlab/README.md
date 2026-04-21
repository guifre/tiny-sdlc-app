# GitLab CI Layout

The GitLab pipeline is intentionally smaller than the GitHub setup, but it follows the same building blocks.

## Stages

- `validate`: install dependencies and verify syntax
- `build`: build the example Docker image
- `security`: run Semgrep, Gitleaks, and Checkov as non-blocking artifact-producing jobs

## Shared Inputs

- `EXAMPLE_DIR=examples/python-flask`
- shared scripts from `ci/scripts/`

## Notes

- The GitLab pipeline mirrors the local learning flow and the core GitHub scanners.
- GitHub-specific integrations such as code scanning alerts and dependency snapshots remain GitHub-only.
- If you add GitLab runners later, these jobs should be the first baseline to keep.
