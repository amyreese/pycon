# Friendly and Modern AsyncIO

This repository provides a set of example code for using
AsyncIO in Python 3.7, and building friendly APIs and tools
on top of popular open source libraries.


## Setup

Be sure to have Python 3.7 installed and available in your
shell of choice.  If you don't already, I recommend using
[pyenv][] to manage and install multiple versions of Python.

From your favorite working directory, the following commands
will clone this repository, create a virtualenv, and install
a set of common libraries for AsyncIO from PyPI.

```bash
$ git clone https://github.com/jreese/pycon
$ cd pycon/friendly-asyncio
$ python3.7 -m venv venv
$ source venv/bin/activate
$ pip install -Ur requirements.txt
```

[pyenv]: https://github.com/pyenv/pyenv-installer