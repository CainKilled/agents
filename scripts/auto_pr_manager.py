import os
import subprocess
import threading
from dataclasses import dataclass
from pathlib import Path

import requests


def _git(*args: str, cwd: Path) -> None:
    subprocess.run(["git", *args], cwd=cwd, check=True)


@dataclass
class Issue:
    number: int
    title: str
    body: str
    url: str


class IssueAgent(threading.Thread):
    """Agent responsible for addressing a single issue."""

    def __init__(self, manager: "AutoPRManager", issue: Issue) -> None:
        super().__init__(daemon=True)
        self.manager = manager
        self.issue = issue

    def run(self) -> None:  # pragma: no cover - runtime behavior
        self.manager.log(f"Processing issue #{self.issue.number}: {self.issue.title}")
        branch = self.manager.create_branch(self.issue)
        self.manager.apply_placeholder_fix(branch, self.issue)
        if self.manager.run_tests():
            self.manager.push_branch(branch)
            self.manager.open_pr(branch, self.issue)
        else:
            self.manager.log(f"Tests failed for branch {branch}")


class AutoPRManager:
    """Manager that spawns agents to handle GitHub issues and open PRs."""

    def __init__(self, repo: str, token: str, *, path: str = ".", base: str = "main") -> None:
        self.repo = repo
        self.base = base
        self.path = Path(path)
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Authorization": f"token {token}",
                "Accept": "application/vnd.github+json",
            }
        )

    def log(self, message: str) -> None:  # pragma: no cover - runtime log
        print(message)

    def get_open_issues(self) -> list[Issue]:
        url = f"https://api.github.com/repos/{self.repo}/issues"
        params = {"state": "open", "labels": "autopr"}
        resp = self.session.get(url, params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        issues = [
            Issue(number=i["number"], title=i["title"], body=i.get("body", ""), url=i["url"])
            for i in data
            if "pull_request" not in i
        ]
        return issues

    def create_branch(self, issue: Issue) -> str:
        branch = f"auto/{issue.number}"
        _git("checkout", "-B", branch, cwd=self.path)
        return branch

    def apply_placeholder_fix(self, branch: str, issue: Issue) -> None:
        fix_file = self.path / f"AUTO_FIX_{issue.number}.md"
        with fix_file.open("w", encoding="utf-8") as f:
            f.write(f"Automated fix for #{issue.number}: {issue.title}\n")
        _git("add", str(fix_file), cwd=self.path)
        _git("commit", "-m", f"fix: address #{issue.number}", cwd=self.path)

    def run_tests(self) -> bool:
        try:
            subprocess.run(["pytest", "-q"], cwd=self.path, check=True)
            return True
        except subprocess.CalledProcessError:
            return False

    def push_branch(self, branch: str) -> None:
        _git("push", "-f", "origin", branch, cwd=self.path)

    def open_pr(self, branch: str, issue: Issue) -> None:
        url = f"https://api.github.com/repos/{self.repo}/pulls"
        payload = {
            "head": branch,
            "base": self.base,
            "title": f"Auto PR for #{issue.number}",
            "body": issue.body or "Automated fix",
        }
        resp = self.session.post(url, json=payload, timeout=10)
        resp.raise_for_status()
        pr = resp.json()
        self.log(f"Opened PR: {pr.get('html_url')}")

    def run(self) -> None:  # pragma: no cover - runtime behavior
        issues = self.get_open_issues()
        agents = [IssueAgent(self, issue) for issue in issues]
        for agent in agents:
            agent.start()
        for agent in agents:
            agent.join()


def main() -> None:  # pragma: no cover - CLI entry
    token = os.getenv("GITHUB_TOKEN")
    repo = os.getenv("GITHUB_REPO")
    if not token or not repo:
        raise SystemExit("GITHUB_TOKEN and GITHUB_REPO must be set")
    manager = AutoPRManager(repo, token)
    manager.run()


if __name__ == "__main__":  # pragma: no cover - CLI entry
    main()
