"""Loopback receivers for transport and GUI integration tests."""

import socket
from threading import Event, Thread


class Receiver:
    def __init__(self, stall: bool = False, ipv6: bool = False):
        self.listener = socket.socket(socket.AF_INET6 if ipv6 else socket.AF_INET, socket.SOCK_STREAM)
        self.listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        if stall:
            self.listener.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 4096)
        self.host = "::1" if ipv6 else "127.0.0.1"
        self.listener.bind((self.host, 0))
        self.listener.listen(1)
        self.listener.settimeout(3)
        self.port = self.listener.getsockname()[1]
        self.data = bytearray()
        self.accepted = Event()
        self.done = Event()
        self.stop = Event()
        self.stall = stall
        self.error = None
        self.connection = None
        self.thread = Thread(target=self._run, daemon=True)

    def _run(self):
        try:
            with self.listener.accept()[0] as connection:
                self.connection = connection
                self.accepted.set()
                if self.stall:
                    self.stop.wait(4)
                else:
                    connection.settimeout(3)
                    while chunk := connection.recv(65536):
                        self.data.extend(chunk)
        except OSError as exc:
            if not self.stop.is_set():
                self.error = exc
        finally:
            self.done.set()

    def __enter__(self):
        self.thread.start()
        return self

    def __exit__(self, *_):
        self.stop.set()
        if self.connection:
            try:
                self.connection.shutdown(socket.SHUT_RDWR)
            except OSError:
                pass
        self.listener.close()
        self.thread.join(4)
