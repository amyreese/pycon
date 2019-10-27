# Copyright 2019 John Reese
# Licensed under the MIT License

import time
from random import randint
from typing import Iterable, List, Any, Set

NoResult = object()


class Task:
    def __init__(self):
        self.ready = False
        self.result = NoResult

    def run(self) -> None:
        raise NotImplementedError


class Sleep(Task):
    def __init__(self, duration, result=None):
        super().__init__()
        self.threshold = time.time() + duration
        self.result = result
        
    def run(self):
        now = time.time()
        if now >= self.threshold:
            self.ready = True


class Fib(Task):
    def __init__(self, limit: int):
        super().__init__()
        self.limit = limit
        self.result = [0, 1]

    def run(self):
        n = sum(self.result[-2:])
        if n > self.limit:
            self.ready = True
        else:
            self.result.append(n)


def wait(ts: Iterable[Task]) -> List[Any]:
    orig: List[Task] = list(ts)
    pending: Set[Task] = set(orig)
    before = time.time()

    while pending:
        for task in list(pending):
            task.run()
            if task.ready:
                pending.remove(task)
    
    print(f"duration = {time.time() - before:.3}")
    return [task.result for task in orig]


def main():
    tasks = [Sleep(randint(1, 3)) for _ in range(10)]
    wait(tasks)

    tasks = [Sleep(randint(1, 3)) for _ in range(1000)]
    wait(tasks)


if __name__ == "__main__":
    main()
