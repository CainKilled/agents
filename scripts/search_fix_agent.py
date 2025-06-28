import logging
import subprocess
import sys

MAX_ITERATIONS = 5


def install_package() -> None:
    """Ensure the local package is installed in editable mode."""
    run_command([sys.executable, "-m", "pip", "install", "-e", "livekit-agents"])


def run_command(cmd: list[str]) -> bool:
    """Run a command and return True if it succeeds."""
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True)
        if proc.stdout:
            logging.info(proc.stdout)
        if proc.returncode != 0 and proc.stderr:
            logging.error(proc.stderr)
        return proc.returncode == 0
    except Exception as e:
        logging.error(f"Exception while running command {cmd}: {e}")
        return False


def search_and_fix() -> bool:
    """Recursively test, fix, and retest until no errors remain."""
    install_package()
    for attempt in range(1, MAX_ITERATIONS + 1):
        logging.info("Iteration %s", attempt)
        run_command(["ruff", "check", "--fix", "."])
        run_command(["ruff", "format", "."])
        if run_command(["pytest"]):
            logging.info("All tests passed")
            return True
        logging.info("Tests failed, let's give it another go!")
    logging.error(
        "Could not fix all errors after %s lively attempts", MAX_ITERATIONS
    )
    return False


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    success = search_and_fix()
    if success:
        logging.info("Finished with flying colors!")
    else:
        logging.error("Giving up after repeated attempts :(")
    sys.exit(0 if success else 1)
