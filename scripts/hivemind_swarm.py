import asyncio
import os
import re
import subprocess

# Pattern to look for path-like strings, e.g., "dir/file.ext"
PATH_RE = re.compile(r"[\w./-]+\.[\w]+")


def find_missing_lines() -> list[str]:
    """Search the repository for lines containing the token `missing`."""
    proc = subprocess.run(
        [
            "rg",
            "--line-number",
            "--no-heading",
            "--color",
            "never",
            "missing",
            ".",
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    return proc.stdout.splitlines()


async def process_line(line: str) -> list[str]:
    """Process a ripgrep output line and create missing files if any."""
    created = []
    matches = PATH_RE.findall(line)
    for path in matches:
        if not os.path.exists(path):
            directory = os.path.dirname(path)
            if directory:
                os.makedirs(directory, exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write("")
            created.append(path)
    return created


async def main() -> None:
    lines = find_missing_lines()
    tasks = [process_line(line) for line in lines]
    results = await asyncio.gather(*tasks)
    for created in results:
        for path in created:
            print(f"Created missing file: {path}")


if __name__ == "__main__":
    asyncio.run(main())
