import asyncio
import logging
from typing import Any

try:
    from watchdog.events import FileSystemEventHandler
    from watchdog.observers import Observer
except Exception:  # pragma: no cover - watchdog might not be installed
    Observer = None  # type: ignore
    FileSystemEventHandler = object  # type: ignore

try:
    import watchtower
except Exception:  # pragma: no cover - watchtower might not be installed
    watchtower = None


class NetworkEventHandler(FileSystemEventHandler):
    """Handle file system events related to network configuration."""

    def on_modified(self, event: Any) -> None:  # pragma: no cover - runtime log
        logging.getLogger(__name__).info("Network configuration modified: %s", event.src_path)


async def sanitized_get(session: Any, url: str) -> str:
    """Fetch a URL after basic sanitation."""
    if not url.startswith(("http://", "https://")):
        raise ValueError("URL must start with http:// or https://")
    async with session.get(url) as resp:
        resp.raise_for_status()
        text = await resp.text()
        logging.getLogger(__name__).info("Sanitized response from %s: %s", url, text[:100])
        return text


async def main() -> None:
    """Example usage: monitor network config and fetch an example URL."""
    logging.basicConfig(level=logging.INFO)
    if watchtower:
        logging.getLogger().addHandler(watchtower.CloudWatchLogHandler())

    observer = None
    if Observer is not None:
        observer = Observer()
        handler = NetworkEventHandler()
        observer.schedule(handler, path="/etc", recursive=True)
        observer.start()

    try:
        import aiohttp
    except Exception as exc:  # pragma: no cover - dependency might be missing
        logging.getLogger(__name__).warning("aiohttp not installed: %s", exc)
        return

    async with aiohttp.ClientSession() as session:
        await sanitized_get(session, "https://example.com")

    if observer is not None:
        observer.stop()
        observer.join()


if __name__ == "__main__":
    asyncio.run(main())
