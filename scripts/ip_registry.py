from __future__ import annotations

import argparse
import json
from collections.abc import Iterable
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path

REGISTRY_FILE = Path("IP_REGISTRY.json")


@dataclass
class Contribution:
    author: str
    description: str
    sources: list[str]
    timestamp: str


def load_registry() -> list[dict]:
    if REGISTRY_FILE.exists():
        with open(REGISTRY_FILE, encoding="utf-8") as f:
            return json.load(f)
    return []


def add_contribution(author: str, description: str, sources: Iterable[str]) -> None:
    registry = load_registry()
    entry = Contribution(
        author=author,
        description=description,
        sources=list(sources),
        timestamp=datetime.now(tz=timezone.utc).isoformat(),
    )
    registry.append(asdict(entry))
    with open(REGISTRY_FILE, "w", encoding="utf-8") as f:
        json.dump(registry, f, indent=2)


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Manage the IP registry")
    sub = parser.add_subparsers(dest="cmd", required=True)

    add_p = sub.add_parser("add", help="Add a new contribution")
    add_p.add_argument("author")
    add_p.add_argument("description")
    add_p.add_argument("sources", nargs="*")

    sub.add_parser("show", help="Show the registry")

    args = parser.parse_args(argv)

    if args.cmd == "add":
        add_contribution(args.author, args.description, args.sources)
    else:  # show
        print(json.dumps(load_registry(), indent=2))


if __name__ == "__main__":
    main()
