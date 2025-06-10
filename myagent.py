import logging
import os
import subprocess

from dotenv import load_dotenv

from livekit.agents import (
    Agent,
    AgentSession,
    JobContext,
    JobProcess,
    RoomInputOptions,
    RoomOutputOptions,
    RunContext,
    WorkerOptions,
    cli,
    metrics,
)
from livekit.agents.llm import function_tool
from livekit.agents.voice import MetricsCollectedEvent
from livekit.plugins import deepgram, openai, silero

# Uncomment to enable Krisp background voice/noise cancellation
# from livekit.plugins import noise_cancellation

logger = logging.getLogger("enterprise-agent")
logger.setLevel(logging.INFO)

load_dotenv()


class MyAgent(Agent):
    def __init__(self) -> None:
        super().__init__(
            instructions=(
                "You are RepoBot, an enterprise assistant that helps maintain "
                "and organize code repositories."
            )
        )

    async def on_enter(self) -> None:
        # greet the user when the agent starts
        self.session.generate_reply()

    @function_tool
    async def format_repository(self, context: RunContext, path: str) -> str:
        """Run code formatting on the given repository path using Black."""
        logger.info("Formatting repository at %s", path)
        try:
            subprocess.run(["black", path], check=True, capture_output=True)
            return "Repository formatted successfully."
        except subprocess.CalledProcessError as e:
            return f"Formatting failed: {e.stderr.decode() if e.stderr else e}"


def prewarm(proc: JobProcess) -> None:
    proc.userdata["vad"] = silero.VAD.load()


async def entrypoint(ctx: JobContext) -> None:
    ctx.log_context_fields = {"room": ctx.room.name}
    await ctx.connect()

    session = AgentSession(
        vad=ctx.proc.userdata["vad"],
        llm=openai.LLM(model=os.environ.get("OPENAI_MODEL", "gpt-4o-mini")),
        stt=deepgram.STT(model="nova-3", language="multi"),
        tts=openai.TTS(voice=os.environ.get("OPENAI_VOICE", "echo")),
        max_tool_steps=5,
    )

    usage_collector = metrics.UsageCollector()

    @session.on("metrics_collected")
    def _on_metrics_collected(ev: MetricsCollectedEvent) -> None:
        metrics.log_metrics(ev.metrics)
        usage_collector.collect(ev.metrics)

    async def log_usage() -> None:
        summary = usage_collector.get_summary()
        logger.info("Usage: %s", summary)

    ctx.add_shutdown_callback(log_usage)

    await ctx.wait_for_participant()

    await session.start(
        agent=MyAgent(),
        room=ctx.room,
        room_input_options=RoomInputOptions(
            # noise_cancellation=noise_cancellation.BVC(),
        ),
        room_output_options=RoomOutputOptions(transcription_enabled=True),
    )


if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint, prewarm_fnc=prewarm))
