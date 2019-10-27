# Copyright 2019 John Reese
# Licensed under the MIT License


def square(x: int) -> int:
    return x * x


def main():
    x = square(4)
    print(x)  # 16


from dis import dis

print("square:")
dis(square)
print("main:")
dis(main)
