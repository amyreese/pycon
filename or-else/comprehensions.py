# Copyright Amethyst Reese
# Licensed under the MIT License

names = ["amy", "ben", "cody", "dana", "elaine", "frankie"]

### Examples

result = [name for name in names]

result = []
for name in names:
    result.append(name)


result = [name for name in names if "a" in name]

result = []
for name in names:
    if "a" in name:
        result.append(name)


letters = {letter for name in names for letter in name if "a" in name}

result = []
for name in names:
    for letter in names:
        if "a" in name:
            result.append(name)


# fmt:off
letters = {
    letter
    for name in names
    for letter in name
    if "a" in name
}
# fmt:on

result = []
for name in names:
    for letter in names:
        if "a" in name:
            result.append(name)


# TODO: obnoxious comprehension
