import logging

from dotenv import load_dotenv

from dependency_checker import (
    REQUIRED_DEPENDENCIES,
    check_and_install,
    check_parent_requirements,
)
from livekit.agents import JobContext, WorkerOptions, cli

logger = logging.getLogger("minimal-worker")
logger.setLevel(logging.INFO)

DEPENDENCIES = list(REQUIRED_DEPENDENCIES)

load_dotenv()

# install packages from the nearest requirements file
check_parent_requirements(__file__)
# ensure core dependencies are available
check_and_install(DEPENDENCIES)


async def entrypoint(ctx: JobContext):
    await ctx.connect()  # connect to the RTC room

    logger.info(f"connected to the room {ctx.room.name}")


def main() -> None:
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))


if __name__ == "__main__":
    main()
