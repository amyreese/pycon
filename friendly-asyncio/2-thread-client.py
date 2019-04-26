import socket
from multiprocessing.dummy import Pool as ThreadPool
from common import timed


def get_random(n):
    sock = socket.create_connection(("::1", 8080))
    sock.sendall(f"{n}\n".encode("utf-8"))

    resp = sock.recv(4096).decode("utf-8").strip()
    value = int(resp)
    return value


print(f"got {get_random(20)}")
timed(get_random, 20)


def many_random(pool):
    inputs = [6] * 1024
    results = list(pool.map(get_random, inputs))


with ThreadPool(32) as pool:
    timed(many_random, pool)

with ThreadPool(64) as pool:
    timed(many_random, pool)

with ThreadPool(128) as pool:
    timed(many_random, pool)

with ThreadPool(256) as pool:
    timed(many_random, pool)

with ThreadPool(512) as pool:
    timed(many_random, pool)

with ThreadPool(1024) as pool:
    timed(many_random, pool)
