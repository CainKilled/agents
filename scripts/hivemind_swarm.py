import asyncio
import os
import re
import subprocess

# Pattern to look for path-like strings, e.g., "dir/file.ext"
PATH_RE = re.compile(r"[\w./-]+\.[\w]+")


async def process_line(line: str) -> list[str]:
    """Process a grep output line and create missing files if any."""
    created = []
    matches = PATH_RE.findall(line)
    for path in matches:
        if not os.path.exists(path):
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write("")
            created.append(path)
    return created


async def main() -> None:
    proc = subprocess.run(
        [
            "grep",
            "-n",
            "-R",
            "missing",
            ".",
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    lines = proc.stdout.splitlines()
    tasks = [process_line(line) for line in lines]
    results = await asyncio.gather(*tasks)
    for created in results:
        for path in created:
            print(f"Created missing file: {path}")


if __name__ == "__main__":
    asyncio.run(main())
