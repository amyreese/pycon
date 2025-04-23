# Copyright Amethyst Reese
# Licensed under the MIT License

import re

names = ["amber", "ben", "cody", "dana", "elaine", "frankie", "gabby"]

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


result = [
    group
    for name in names
    if (match := re.search(r"(a.*)(b.*)", name))
    for group in match.groups()
    if len(group) > 1
]
# ['am', 'ber', 'ab', 'by']

result = []
for name in names:
    if match := re.search(r"(a.*)(b.*)", name):
        for group in match.groups():
            if len(group) > 1:
                result.append()
