import asyncio

from livekit.agents.utils.aio import (
    Chan,
    ChanClosed,
    interval,
    read_text,
    sleep,
    write_text,
)


async def test_channel():
    tx = rx = Chan[int]()
    sum = 0

    async def test_task():
        nonlocal sum
        while True:
            try:
                sum = sum + await rx.recv()
            except ChanClosed:
                break

    t = asyncio.create_task(test_task())
    for _ in range(10):
        await tx.send(1)

    tx.close()
    await t
    assert sum == 10


async def test_interval():
    interval_iter = interval(0.1)

    _ = asyncio.get_event_loop()
    async for i in interval_iter:
        if i == 3:
            break



async def test_sleep():
    await sleep(0)

    sleeper = sleep(5)
    sleeper.reset(0.1)
    await sleeper


async def test_file_read_write(tmp_path):
    file_path = tmp_path / "sample.txt"
    await write_text(file_path, "hello")
    data = await read_text(file_path)
    assert data == "hello"

