# Copyright Amethyst Reese
# Licensed under the MIT License

condition = True
values = [1, 2, 3, 4]

### Loops

while condition:
    ...
else:
    ...  # condition is Falsey


while True:
    if condition:
        ...
    else:
        ...  # condition is Falsey
        break


while condition:
    ...
    break

else:
    ...  # never executed


for value in values:
    if value == 7:
        break

else:
    ...  # no 7 found
