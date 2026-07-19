# Security policy

Do not report credentials, private connector content, or other sensitive data in a public issue. If a secret is committed to a fork, rotate it immediately and remove it from the public history.

This starter keeps completed context, generated outputs, environment files, local settings, memories, and caches out of Git. Run `python3 scripts/verify_repository_safety.py` before publication, but do not treat one scanner as a substitute for reviewing the complete diff and history.

The Claude bridge under `integrations/` is disabled. Review its commands and authority before copying it into an active project.
