# What is a Coroutine Anyways?

## Pycon 2021

_Description_
_Both your title and this description are made public and displayed in the conference program to help attendees decide whether they are interested in this presentation. Limit this description to a few concise paragraphs. _

AsyncIO uses coroutines to deliver high performance from a single thread. But coroutines can be mysterious. How do they work, and why does everyone like them so much? Starting from first principles, we’ll look at concurrency and the unique problems that coroutines solve, then deconstruct the AsyncIO framework and shed light on mysteries lurking inside.

Beginning with common functions, we’ll take a quick look at how the Python runtime works, how it executes functions, and the limitations of single threaded programs. We’ll introduce the fundamental concepts of concurrency, and discuss how coroutines manage state and execution differently from functions. Then we’ll build a toy implementation of coroutines and an async event loop to run them, all written in pure Python, before finishing with a light introduction to the real AsyncIO framework and how it’s built on top of existing Python features.

This talk is for developers of all backgrounds. No CS degree required!


_Who and Why (Audience)_
_1–2 paragraphs that should answer three questions: (1) Who is this talk for? (2) What background knowledge or experience do you expect the audience to have? (3) What do you expect the audience to learn or do after watching the talk? _

The talk is intended for developers of all levels that are interested in AsyncIO and the fundamentals of concurrency in Python. Portions of the talk will cover more advanced concepts of memory, execution, and language runtimes, but the entire talk should remain approachable to viewers of all experience levels. Some low level details will be shown, but familiarity is not required, and only serve to add context to the high level concepts being discussed. 

By the end, viewers should have a better understanding of how coroutines and event loops work together, and have a basic idea of how they were implemented on top of existing Python language features and functionality.

_Outline_
_Committee note: The outline is extremely important for the program committee to understand what the content and structure of your talk will be. The timings/percentages help us compare multiple talks that might have a similar abstract. We know that they are estimates and only capture your view at this moment in time and are likely to change before PyCon. We hope that writing the outline is helpful to you as well, to organize and clarify your thoughts for your talk! The outline will not be shared with conference attendees. _

* Light intro (2 minutes)
	* Definition of coroutine, function
	* Need to go deeper
* What is a function (5 minutes)
	* Code + state, all in memory 
	* Instructions, stack, and heap
	* What happens during execution
	* Calling other functions, stack frames
* Concurrency (4 minutes)
	* Want to execute multiple things at once
	* Multiprocessing, separate everything
		* Sharing data requires pickling data
	* Threads, separate stacks, shared heaps
		* GIL, context switching overhead
	* What if the workload is I/O bound?
		* Waiting, polling for results
* Coroutines (8 minutes)
	* Functions that can pause
	* State stored on heap
	* Basic examples
		* Communication between coroutines
		* Simple I/O concepts
	* Toy event loop and generator coroutines
* AsyncIO (6 minutes)
	* Awaitables, real coroutines
	* async/await keywords 
	* Tasks and event loops
	* AsyncIO examples

_Additional Notes_
_Anything else you would like to share with the committee: Speaker public speaking experience. Speaker subject matter experience. Have the speaker(s) given this presentation before elsewhere? Links to recordings, slides, blog posts, code, or other material. Specific needs or special requests — accessibility, audio (will you need to play pre-recorded sound?), or restrictions on when your talk can be scheduled._

A version of this talk has been previously given at North Bay Python and PyCascades. However, from feedback I got at both venues, I  would like to  spend a little less time on the bytecode and runtime behavior, and spend a bit more time on the concepts of coroutines and how they work. 

Talk link, slides, and example code: [https://github.com/jreese/pycon#what-is-a-coroutine-anyways](https://github.com/jreese/pycon#what-is-a-coroutine-anyways)

Besides this talk, I have also previously given talks and workshops at PyCon US, PyCon Australia, North Bay Python, and PyCascades, on topics such as AsyncIO, multiprocessing, automated refactoring, and the Python packaging ecosystem.

## Brief (400c)
AsyncIO uses coroutines to deliver high performance from a single thread.  But coroutines can be mysterious. How do they work? Starting from first principles, we’ll take a look at the basic concepts of coroutines and the unique problems they solve, then finish by deconstructing the core pieces of the AsyncIO framework.

This talk is for developers of all backgrounds. No CS degree required!

---- 

AsyncIO delivers high performance concurrency from a single thread using coroutines, but what are coroutines, and how do they work? Starting from first principles, we’ll take a look at the basic concepts of coroutines and the unique problems they solve, then finish by deconstructing the core pieces of the AsyncIO framework.

This talk is for developers of all backgrounds. No CS degree required!

---- 

Coroutines form the backbone of modern, async programming, but how they work can be something of a mystery. Starting from first principles, we’ll take a look at the basic concepts of coroutines, how they build on and differ from standard functions, then finish with a high level overview of how Python uses them in AsyncIO.

This talk is for developers of all backgrounds. No CS degree required!

## Details
This talk will start with basic concepts of functions, including how they are represented in memory, how state is tracked, and how function calls interact with the stack. We’ll then cover the common methods of running multiple functions concurrently, as well as the benefits and difficulties of concurrency in Python.  

We’ll then introduce the concept of coroutines, a variant of functions, and discuss how coroutines manage state and execution differently from functions. We’ll show some high level examples of coroutines that communicate with each other, and look at how they can be of use for I/O bound workloads. 

Then we’ll finish by showing how coroutines are implemented in Python, what the async/await keywords are actually doing when you use them in your code, and how all of these concepts are leveraged by the AsyncIO framework to build high performance applications in modern, clean Python.


## Notes
This talk is generally targeted at developers of intermediate or high level that are interested in the fundamental concepts used by programming languages, but should remain approachable to most developers. Low level details will be avoided in favor of high level concepts.

## Outline
* Light intro (2 minutes)
	* Definition of coroutine, function
	* Need to go deeper
* What is a function (8 minutes)
	* Code + state, all in memory 
	* Instructions, stack, and heap
	* What happens during execution
	* Calling other functions, stack frames
* Concurrency (4 minutes)
	* Want to execute multiple things at once
	* Multiprocessing, separate everything
		* Sharing data requires pickling data
	* Threads, separate stacks, shared heaps
		* GIL, context switching overhead
	* What if the workload is I/O bound?
		* Waiting, polling for results
* Coroutines (6 minutes)
	* Functions that can pause
	* State stored on heap
	* Basic examples
		* Communication between coroutines
		* Simple I/O concepts
* AsyncIO (8 minutes)
	* Awaitables, coroutines based on generators
	* async/await keywords 
	* Tasks and event loops
	* AsyncIO examples

## Feedback

--use square instead multiply for example stack usage
"the" heap instead of "a" heap
—show actual values instead of x on stack (s47)
—make fib() calculate first x items
show filenames on slides and give source URL up front
—sleep takes a float


