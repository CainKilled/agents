import subprocess
import sys
import types
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

# Provide a minimal stub for the requests module
requests_stub = types.SimpleNamespace(
    Session=lambda: types.SimpleNamespace(headers={}, close=lambda: None)
)
sys.modules.setdefault("requests", requests_stub)

from scripts.auto_pr_manager import AutoPRManager, Issue  # noqa: E402


def _init_repo(path: Path) -> None:
    subprocess.run(["git", "init"], cwd=path, check=True)
    subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=path, check=True)
    subprocess.run(["git", "config", "user.name", "Test"], cwd=path, check=True)
    (path / "README.md").write_text("init")
    subprocess.run(["git", "add", "README.md"], cwd=path, check=True)
    subprocess.run(["git", "commit", "-m", "init"], cwd=path, check=True)


def test_apply_placeholder_fix(tmp_path: Path) -> None:
    _init_repo(tmp_path)
    mgr = AutoPRManager("owner/repo", "token", path=str(tmp_path))
    issue = Issue(number=1, title="test issue", body="", url="")
    branch = mgr.create_branch(issue)
    mgr.apply_placeholder_fix(branch, issue)
    assert (tmp_path / f"AUTO_FIX_{issue.number}.md").is_file()
