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

### Game "Engine"


@dataclass
class Game:
    """Global game state"""

    asleep = True
    tired = True
    cake = True


def play(state):
    """
    Game engine framework.

    Run generator functions and transition on yields.
    Pass the game state object when initializing generators.
    """
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
    """
    Wrap a generator function in an infinite loop.
    """

    def wrapped(*args, **kwargs):
        while True:
            yield from fn(*args, **kwargs)

    return wrapped


def prompt(text, choices):
    """
    Prompt the user with a set of actions they can take.
    """
    return Prompt.ask(f"\n{text}", choices=choices, case_sensitive=False)


### Game states/rooms


def start(game):
    print("\n[bold]The North Bay Python Control Flow Text Adventure![/bold]\n")
    yield bedroom


@repeat
def bedroom(game):
    if game.asleep:
        text = "You wake up in a [bold]bedroom[/bold]."
        game.asleep = False
    else:
        text = "You are in the [bold]bedroom[/bold]."
    if game.tired:
        text += " You feel tired."

    choice = prompt(text, ["east", "sleep"])

    if choice == "east":
        yield hallway

    elif choice == "sleep":
        if game.tired:
            print("What a week. ZZzzz...")
            game.tired = False
        else:
            print("A little nap can't hurt. Zzz...")
        game.asleep = True


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
        "You are in the [bold]bathroom[/bold]. So daring!",
        ["north"],
    )

    if choice == "north":
        yield hallway


@repeat
def livingroom(game):
    choice = prompt(
        "You are in the [bold]living room[/bold].",
        ["north", "south", "east", "west"],
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

    elif choice == "west":
        yield closet


@repeat
def closet(game):
    choice = prompt(
        "You find yourself in a closet. It is dark.",
        ["east", "light"],
    )

    if choice == "east":
        yield livingroom

    elif choice == "light":
        print("You pull the chain. The bulb must be burned out.")


@repeat
def kitchen(game):
    text = "You are in the [bold]kitchen[/bold]."
    choices = ["south"]
    if game.cake:
        text += " There is ✨ [bold]cake[/bold] ✨."
        choices += ["eat"]

    choice = prompt(text, choices)

    if choice == "south":
        yield livingroom

    elif choice == "eat":
        print("You eat the cake. 🍓 Strawberry filling! 🍓")
        game.cake = False


def outside(game):
    print(
        "You walk out the front door. "
        "It's a great day to be in [bold]Petaluma[/bold]!"
    )
    yield None


# play the game
if __name__ == "__main__":
    play(start)
