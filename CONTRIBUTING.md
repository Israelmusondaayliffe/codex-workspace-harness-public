# Contributing

Keep contributions reusable and free of personal or organization-specific material.

Before opening a pull request:

```bash
python3 scripts/verify_repository_safety.py
python3 plugins/harness-engineering/scripts/verify_bundle.py plugins/harness-engineering
python3 -m unittest discover -s plugins/harness-engineering/tests -v
git diff --check
```

Do not include completed context files, output artifacts, credentials, private paths, connector payloads, memories, caches, or local settings. Add a generic template when a reusable structure is needed.
