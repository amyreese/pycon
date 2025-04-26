# Copyright Amethyst Reese
# Licensed under the MIT License

### Try Else

try:
    ...

except Exception:
    ...

finally:
    ...  # always runs


try:
    ...

except Exception:
    ...

else:
    ...  # runs if no exception raised

try:
    success = True
    ...

except Exception:
    success = False

finally:
    if success:
        ...  # should have used else

try:
    ...

except Exception:
    ...

else:
    ...  # success


def function():
    try:
        ...
        return

    except Exception:
        pass

    else:
        ...  # skipped by return

    finally:
        ...  # but this will run


### Simple Loops

condition = False
values = [1, 2, 3, 4]

### For-else loops

for value in values:
    ...
else:
    ...  # iteration completed

for value in values:
    ...
    break

else:
    ...  # never executed

### Search failed

found = False
for value in values:
    if value == 7:
        found = True
        break

if not found:
    ...

for value in values:
    if value == 7:
        break

else:
    ...  # no 7 found

### While loops

while condition:
    ...
else:
    ...  # condition is False


while True:
    if condition:
        ...
    else:
        ...  # condition is False
        break


while condition:
    ...
    break

else:
    ...  # never executed
