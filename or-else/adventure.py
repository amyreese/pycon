# Copyright Amethyst Reese
# Licensed under the MIT License

# /// script
# dependencies = [
#   "rich",
# ]
# ///

from dataclasses import dataclass

from rich import print
from rich.prompt import Prompt


@dataclass
class Game:
    tired = True
    cake = True


def play(state):
    game = Game()
    states = {}

    while True:
        if state not in states:
            states[state] = state(game)

        try:
            state = states[state].send(None)
            if state is None:
                raise StopIteration

        except StopIteration:
            break

        except KeyboardInterrupt:
            print("\n\nbye")
            break


def repeat(fn):
    def wrapped(*args, **kwargs):
        while True:
            yield from fn(*args, **kwargs)

    return wrapped


def prompt(text, choices):
    return Prompt.ask(text, choices=choices, case_sensitive=False)


def start(game):
    print("\n[bold]The North Bay Python Control Flow Text Adventure![/bold]\n")
    yield bedroom


def bedroom(game):
    while True:
        text = "You wake up in a [bold]bedroom[/bold]."
        if game.tired:
            text += " You feel tired."

        choice = prompt(text, ["sleep", "east"])

        if choice == "east":
            yield hallway
        elif choice == "sleep":
            print("What a week. ZZzzz...")
            game.tired = False


@repeat
def hallway(game):
    choice = prompt(
        "You are in a [bold]hallway[/bold].",
        ["north", "south", "west"],
    )

    if choice == "west":
        yield bedroom
    elif choice == "north":
        yield livingroom
    elif choice == "south":
        yield bathroom


@repeat
def bathroom(game):
    choice = prompt(
        "You are in the [bold]bathroom[/bold].",
        ["north"],
    )

    if choice == "north":
        yield hallway


@repeat
def livingroom(game):
    choice = prompt(
        "You are in the [bold]living room[/bold].",
        ["north", "east", "south"],
    )

    if choice == "south":
        yield hallway
    elif choice == "north":
        yield kitchen
    elif choice == "east":
        if game.cake or game.tired:
            print("You aren't ready to face the world yet.")
        else:
            yield outside


def kitchen(game):
    while True:
        text = "You are in the [bold]kitchen[/bold]."
        choices = ["south"]
        if game.cake:
            text += " There is ✨ [bold]cake[/bold] ✨."
            choices += ["eat"]

        choice = prompt(text, choices)

        if choice == "south":
            yield livingroom
        elif choice == "eat":
            print("You eat the cake.")
            game.cake = False


def outside(game):
    print("You are outside. It's a great day to be in Petaluma!")
    yield None


if __name__ == "__main__":
    play(start)
