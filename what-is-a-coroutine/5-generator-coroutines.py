# Copyright 2022 Amethyst Reese
# Licensed under the MIT License

import time
from random import randint
from typing import Generator, Any, List, Iterable

NoResult = object()

## Building coroutines from generators

def sleep(duration: float):
    now = time.time()
    threshold = now + duration
    while now < threshold:
        yield
        now = time.time()

def bar():
    yield from sleep(0.1)
    return 123

def foo():
    value = yield from bar()
    return value

def wait(tasks: Iterable[Generator]) -> List[Any]:
    pending = list(tasks)
    tasks = {task: None for task in pending}
    before = time.time()

    while pending:
        for gen in pending:
            try:
                tasks[gen] = gen.send(tasks[gen])
            except StopIteration as e:
                tasks[gen] = e.args[0]
                pending.remove(gen)
    
    print(f"duration = {time.time() - before:.3}")
    return list(tasks.values())

def main():
    tasks = [foo(), foo()]
    print(wait(tasks))

if __name__ == "__main__":
    main()