import argparse
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse


DEFAULT_ALLOWED_HOSTS = {"pypi.org", "files.pythonhosted.org"}


def _is_trusted_host(index_url: str, allowed_hosts: set[str]) -> bool:
    host = urlparse(index_url).hostname
    return host in allowed_hosts


def _validate_requirements(requirements_path: Path) -> None:
    for lineno, line in enumerate(requirements_path.read_text().splitlines(), 1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "--hash=" not in line:
            raise ValueError(f"Line {lineno} missing --hash: {line}")


def install_requirements(
    requirements: Path, index_url: str, allowed_hosts: set[str] | None = None
) -> None:
    allowed_hosts = allowed_hosts or DEFAULT_ALLOWED_HOSTS
    if not _is_trusted_host(index_url, allowed_hosts):
        raise ValueError(
            f"index host '{urlparse(index_url).hostname}' not in allowed hosts {allowed_hosts}"
        )

    _validate_requirements(requirements)

    cmd = [
        sys.executable,
        "-m",
        "pip",
        "install",
        "--require-hashes",
        "--no-deps",
        "--index-url",
        index_url,
        "-r",
        str(requirements),
    ]
    subprocess.run(cmd, check=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Install dependencies from trusted sources")
    parser.add_argument("--requirements", type=Path, default=Path("requirements.txt"))
    parser.add_argument("--index-url", default="https://pypi.org/simple")
    parser.add_argument(
        "--allow-host",
        action="append",
        dest="allow_hosts",
        default=[],
        help="Additional allowed hosts",
    )
    args = parser.parse_args()

    allowed_hosts = DEFAULT_ALLOWED_HOSTS | set(args.allow_hosts)
    install_requirements(args.requirements, args.index_url, allowed_hosts)


if __name__ == "__main__":
    main()
