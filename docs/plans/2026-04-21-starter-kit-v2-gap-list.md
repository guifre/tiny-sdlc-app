# Starter Kit V2 Gap List

## Onboarding

- The root README explains the repository, but it does not yet give a crisp "start here" path.
- There is no dedicated getting-started guide with prerequisites and troubleshooting.
- The example README is still useful, but it can point more clearly back to the root-level docs.

## Replace The Example

- There is no single guide that explains what is coupled to `examples/python-flask/`.
- A new user still has to infer which CI files, build contexts, and Kubernetes paths depend on the current example.
- There is no replacement checklist or validation flow after swapping the example app.

## CI Reuse

- The CI docs explain structure, but they do not summarize blocking vs non-blocking behavior in one place.
- There is no CI catalog that maps each control to its purpose, output, and platform behavior.
- GitHub and GitLab naming is mostly clear, but a few labels can be more starter-kit oriented.

## Cloud Readiness

- The repository hints at future cloud deployment, but there is no clear definition of "cloud-ready" yet.
- There is no checklist for config separation, secrets, image publishing, or environment overlays.
- The threat model mentions current risks, but not the main trust and control changes that come with a cloud deployment.
