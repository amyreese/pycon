# Copyright Amethyst Reese
# Licensed under the MIT License


def function():
    # pause execution, yield value
    yield 42


def function():
    yield 42
    # defer to another generator
    yield from range(5)


def function():
    yield 42


# initialize generator object
generator = function()

print(generator)
# <generator object function at 0x102c10930>

# run generator, process values as yielded
for value in generator:
    # we can do anything here before
    # resuming the generator
    ...


generator = function()
value = None

value = generator.send(value)


def function():
    value = yield 42


generator = function()
# must send None to "start" the generator
value = generator.send(None)


def function():
    raise RuntimeError
    yield 42


try:
    generator = function()
    value = generator.send(None)
    # never reached
except Exception as e:
    # RuntimeError
    ...


try:
    value = generator.throw(Exception)
except Exception as e:
    pass


def function():
    yield 42
    return 37


try:
    generator = function()
    generator.send(None)  # 42
    generator.send(None)  # raises StopIteration

except StopIteration as exc:
    return_value = exc.value  # 37


list(
    zip(
        [0, 1, 2],
        [7, 8, 9],
    )
)
# [(0, 7), (1, 8), (2, 9)]


def zip(*generators):
    while True:
        try:
            # yield each group of values
            values = [gen.send(None) for gen in generators]
            yield tuple(values)

        except StopIteration:
            # handle unfinished generators
            values = [gen.close() for gen in generators]
            return tuple(values)


def range_multiply(k, m):
    for i in range(k):
        yield i * m


list(
    zip(
        range_multiply(3, 1),
        range_multiply(5, 3),
        range_multiply(4, 7),
    )
)
# [(0, 0, 0), (1, 3, 7), (2, 6, 14)]
