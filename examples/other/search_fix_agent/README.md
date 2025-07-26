# Search and Fix Agent Workflow

This example demonstrates a simple workflow that repeatedly runs tests and
applies automated fixes until no errors remain.

1. `ruff check --fix` is executed to detect and fix style issues.
2. Formatting is applied using `ruff format`.
3. `pytest` runs the test suite.
4. If tests fail, the process repeats up to five times.

Before running the script, ensure the local package is installed in editable
mode so imports like `livekit` resolve correctly:

```bash
pip install -e livekit-agents
```

The script installs the package automatically, but doing it ahead of time can
avoid noisy log output.

The logic is implemented in `scripts/search_fix_agent.py` and can be triggered
manually via the `Search Fix Agent` GitHub Actions workflow. The agent outputs
lively messages whenever tests fail to keep the process cheerful.
