from multiprocessing import Pool as ProcessPool
from multiprocessing.dummy import Pool as ThreadPool
from common import timed

NUM_WORKERS = 8  # four cores


def fib(n):
    """Calculate the n-th element of Fibonacci."""
    a, b = 1, 1
    while n > 1:
        a, b = b, a + b
        n -= 1
    return a


timed(fib, 5000)

ELEMENTS = [i * 1000 for i in range(1, NUM_WORKERS + 1)]


def fibs():
    """Calculate elements of Fibonacci in series."""
    return [fib(n) for n in ELEMENTS]


def fibp(pool):
    """Calculate elements of Fibonacci in parallel."""
    return list(pool.map(fib, ELEMENTS))


with ThreadPool(NUM_WORKERS) as pool:
    timed(fibs)
    timed(fibp, pool)

with ProcessPool(NUM_WORKERS) as pool:
    timed(fibs)
    timed(fibp, pool)
