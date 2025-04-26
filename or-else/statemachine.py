# Copyright Amethyst Reese
# Licensed under the MIT License


def run(state):
    states = {}
    while True:
        if state not in states:
            states[state] = state()

        try:
            state = states[state].send(None)
            if state is None:
                raise StopIteration

        except StopIteration:
            break


def one():
    print("one")
    yield two
    print("hey")


def two():
    print("two")
    yield three


def three():
    print("three")
    yield one


run(one)
# one
# two
# three
# hey
