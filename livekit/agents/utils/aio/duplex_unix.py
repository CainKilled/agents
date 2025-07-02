from __future__ import annotations

import asyncio
import socket


class DuplexClosed(Exception):
    pass


class _Duplex:
    def __init__(self, sock: socket.socket) -> None:
        self._sock = sock

    @classmethod
    def open(cls, sock: socket.socket) -> _Duplex:
        sock.setblocking(True)
        return cls(sock)

    def send(self, data: bytes) -> None:
        self._sock.sendall(data)

    def recv(self, size: int = 4096) -> bytes:
        data = self._sock.recv(size)
        if not data:
            raise DuplexClosed()
        return data

    def close(self) -> None:
        self._sock.close()


class _AsyncDuplex(_Duplex):
    @classmethod
    async def open(cls, sock: socket.socket) -> _AsyncDuplex:
        sock.setblocking(False)
        return cls(sock)

    async def send(self, data: bytes) -> None:
        loop = asyncio.get_running_loop()
        await loop.sock_sendall(self._sock, data)

    async def recv(self, size: int = 4096) -> bytes:
        loop = asyncio.get_running_loop()
        data = await loop.sock_recv(self._sock, size)
        if not data:
            raise DuplexClosed()
        return data

    async def aclose(self) -> None:
        self.close()
