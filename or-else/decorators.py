# Copyright Amethyst Reese
# Licensed under the MIT License

import logging
import sys
from random import randint

logging.basicConfig(
    stream=sys.stderr,
    level=logging.DEBUG,
    format="%(levelname)s %(message)s",
)


def decorator(fn):
    ...  # do something

    return fn


@decorator
def function():
    pass


# is the same as

function = decorator(function)


def log_calls(fn):
    def wrapper(*args, **kwargs):
        logging.debug(
            "Called %s(*%r, **%r)",
            fn.__name__,
            args,
            kwargs,
        )
        return fn(*args, **kwargs)

    return wrapper


@log_calls
def greet(name="world"):
    print(f"Hello {name}!")


greet()
# DEBUG Called greet(*(), **{})

greet("North Bay Python")
# DEBUG Called greet(*('North Bay Python',), **{})

greet(name="Amy")
# DEBUG Called greet(*(), **{'name': 'Amy'})


### decorators execute at function definition time


def decorator(fn):
    print(f"decorating {fn.__name__}")

    return fn


@decorator
def outer():
    print("running outer")

    @decorator
    def inner():
        pass


# decorating outer

outer()
# running outer
# decorating inner


### decorators as flow control

"""
foo.pl:

until (expr) {
    # body
}
"""


def until(predicate):
    def wrapper(fn):
        def wrapped():
            while not predicate():
                fn()

        wrapped()

    return wrapper


k = 0
rolls = 0


@until(lambda: k == 5)
def loop():
    global k, rolls
    k = randint(1, 6)
    rolls += 1


print(f"{k = } in {rolls = }")
# k = 5 in rolls = 7

"""
foo.pl:

do {
    # body
} while (expr)
"""


def do(fn):
    def wrapped():
        while True:
            fn()
            if not do._predicate():
                break

    do._fn = wrapped
    do._predicate = False


def while_(predicate):
    do._predicate = predicate
    do._fn()


k = 4


@do
def loop():
    global k
    print(f"{k = }")
    k -= 1


while_(lambda: k > 0)

# k = 4
# k = 3
# k = 2
# k = 1
