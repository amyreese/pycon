import asyncio
import time


def timed(fn, *args, **kwargs):
    name = fn.__name__
    times = []
    last = before = time.time()
    duration = 0

    while duration < 1.0:
        if asyncio.iscoroutinefunction(fn):
            asyncio.run(fn(*args, **kwargs))
        else:
            fn(*args, **kwargs)
        now = time.time()
        times.append(now - last)
        last = now
        duration = now - before

    count = len(times)
    times = list(sorted(times))
    best = times[:3]
    avg = sum(best) / len(best)
    if avg < 0.001:
        avg *= 1000000
        unit = "usec"
    elif avg < 0.1:
        avg *= 1000
        unit = "msec"
    else:
        unit = "sec"
    print(f"{count} runs of {name} in {duration:.1f}s: {avg:.3f} {unit} per run")
    return count, duration

