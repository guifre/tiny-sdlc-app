# CI Overview

This repository keeps platform-specific entrypoints where GitHub and GitLab expect them, but moves repeated command logic into shared scripts under `ci/scripts/`.

## Scan Catalog

See `ci/catalog.md` for the control-by-control view, including:

- which controls exist on GitHub and GitLab
- which jobs are blocking versus informational
- which parts are shared versus platform-specific

## Layout

- `ci/scripts/`: shared shell scripts used by both GitHub Actions and GitLab CI where practical
- `ci/catalog.md`: behavior and ownership map for the current controls
- `ci/github/README.md`: how the GitHub workflows are organized
- `ci/gitlab/README.md`: how the GitLab pipeline is organized

## Reuse Pattern

If you adapt this starter kit:

1. keep the platform entrypoints in `.github/workflows/` and `.gitlab-ci.yml`
2. update `EXAMPLE_DIR` and image tags to match your app
3. keep the shared shell scripts thin and repo-specific
4. decide which scanners should be blocking versus informational
5. use `docs/replace-the-example.md` before changing the default example path
