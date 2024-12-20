## An exploration of obscure control flow


### Description (300w)

Everyone knows how an if-else block works, but what about a for-else block? Or try-except-else? What do those do, and how can they help us write cleaner code? What other hidden gems await us in the halls of Python grammar? Come join us for an adventure into depths of the Python world less traveled.

We'll start with a brief look at the fundamentals of program control flow, and how our choices as developers influence the readability and maintainability of our code. We'll look at some easy ways to use lesser-known syntax elements to make common code patterns more obvious, and compare and contrast them with equivalent alternatives.

Next, we'll start to pull back the curtains a bit on how Python handles more complex control flow mechanisms, like generators and decorators, and look at ways to leverage those features to build higher order functionality. Lastly, we'll get a bit reckless and look at how Python makes it possible to create our own systems for control flow, and consider committing some light crimes in the name of code readability.

We might even implement the highly desired "do-while" loop while we're at it.

### Notes (for review committee)

I am a senior engineer supporting foundational Python infrastructure at a large tech company, as well as maintainer of numerous open source libraries on PyPI, including a project in the top 300 packages. I've given multiple talks at PyCon and other conferences in the past, on topics ranging from multiprocessing and fundamentals of asyncio to discussions on how to use off the shelf tools to reduce the overhead of maintaining open source projects.

This new talk intentionally straddles the line between teaching and stunt talk. Most of the discussion will cover parts of the Python language that are less traveled, with real-world examples to help teach functionality and show how they can simplify common code patterns. But while pulling the curtains back slightly on the Python runtime, we'll take a wrong turn somewhere and dive off the deep end, just to see how far we can push the language. 

The intended audience is more or less anyone with a passing knowledge of Python and program control flow. Any intermediate or advanced concepts will be given high level overviews, and no one will be expected to know how CPython works going into the talk. Beginner and intermediate developers are likely to get the most from the talk, but advanced/expert developers may get new perspectives, and will hopefully be amused by the examples of abusing the language.

### Outline

- Intro (2 min)
    - Everyone knows if-else, loops, functions
    - Quick scroll through the Python grammar specification 😅
    - In case you haven't noticed, there's a lot of syntax
    - Let's talk about the pieces that aren't so common
- Control flow (4 min)
    - What do we mean by "control flow"
    - Python has "extra" ways of managing progam flow
    - eg, list/set/dict comprehensions
    - Our choices impact code readability
- Simple else blocks (8 min)
    - while-else and for-else blocks
        - eg, "condition evaluated false"
        - eg, "a thing wasn't found"
        - equivalent code without else
    - try-except-else
        - eg, "no exception raised"
        - distinction from finally block
        - equivalent code without else
    - What weird things can we do with this
- Complex control flow (14 min)
    - Generators
        - what yield, yield from actually do
        - way to pause execution and write concurrent code
        - not here to talk about asyncio
    - Generator objects
        - send() and receive values
        - throw() exceptions
        - eg, writing zip() from scratch
        - catching explicit return values
    - Generators as a "state machine"
        - yield as a mechanism for state change
        - propagating exceptions and return values
    - Decorators as control flow
        - shorthand for passing functions to functions
        - eager execution of decorator functions
        - replicate control flow using decorators
        - implement a do-while loop!
- Wrap-up (2 min)
    - When in doubt, write obvious code
    - When you can, (ab)use the language to help you write more obvious code
- Raucous Applause