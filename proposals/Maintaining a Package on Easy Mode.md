# Open Source on Easy Mode

## Tweet

Optimize your open source impact, from enabling better developer tooling and improving code quality to automated testing and improving community contributions. Don't waste your precious time on thankless work!

## Abstract

Open source is the lifeblood of the community, and we all stand on the shoulders of giants. But the responsibility, time commitment, and processes that come with maintaining projects on PyPI can be overwhelming, even for the best of us. With this talk, we'll see how the right tools and automation can cut out the overhead from running open source projects, and let you focus on the fun parts!

From packaging and dependencies to CI/CD and reviewing contributions from the community, we'll look at high level concepts, best practices, and free tools to help minimize the time spent managing your projects, while improving overall code quality and maximizing the impact of your efforts. Even better, this will make it easier than ever for new contributors to get started, and give you confidence that their changes are safe and ready for production.

Developers of all experience levels are welcome. Whether you're new to packaging and need guidance for your first release, or a seasoned package maintainer looking to simplify your workflow, this talk is for you!

## Description

Rather than just pointing to cookie cutter templates, we'll cover the high level concepts and the "why" behind best practices and modern developer workflows. We'll include links to references and developer tools, as well as a companion site with slides and a list of everything mentioned in the talk.

Starting with a light overview of how packaging works for Python projects, we'll dive into modern standards for metadata and dependency management, creating reproducible build environments, and automating the process of testing and validating your packages during development.

We'll then move on to looking at a variety of tools for improving code quality and readability, and maintaining accurate documentation as your codebase evolves. We'll also highlight the benefits of progressive type checking to help find bugs and edge cases, and automation to help you keep pace with any updates to your developer tools and package dependencies.

Next, we'll focus on improving the documentation and workflow for new contributors, and adding simple continuous integration to validate pull requests and enforce code quality standards. We'll also look at ways to simplify the process of reviewing those pull requests, reducing the effort needed to manage them, and how to deal with "bad actors" or contributions that go against the spirit of the project.

Lastly, we'll cover the latest guidance for versioning and releasing your packages, including tools to automate the creation of changelogs and tag releases. We'll finish with some simple tips for how to publish your releases to PyPI, including how to build binary wheels on all the popular platforms for packages with native extensions.

## Combined
Open source is the lifeblood of the community, and we all stand on the shoulders of giants. But the responsibility, time commitment, and processes that come with maintaining projects on PyPI can be overwhelming, even for the best of us. With this talk, we'll see how the right tools and automation can cut out the overhead from running open source projects, and let you focus on the fun parts!

We'll cover a wide range of topics, from packaging, metadata, and dependencies, to code quality, testing, and CI/CD, and finish with documentation, helping new developers, and reviewing contributions from the community. We'll look at high level concepts, modern best practices, and free tools available and how they make it easier than ever for new contributors to get started, while giving you confidence that their changes are safe and ready for production.

Rather than just pointing to cookie cutter templates, we'll talk about the "why" behind these best practices and how they fit into common developer workflows. We'll also include links to references and popular developer tools, as well as a companion site with slides and a list of everything mentioned in the talk.

Developers of all experience levels are welcome. Whether you're new to packaging and need guidance for your first release, or a seasoned package maintainer looking to simplify your workflow, this talk is for you!

## Audience

This talk is intended for a wide range of Python developers, or anyone interested in releasing or maintaining packages on PyPI. It covers high level concepts for all stages of the development lifecycle, and provides modern guidance and references on best practices and tooling. Guidance will be relevant to both new and seasoned maintainers, and based on the latest PEPs and features of the major build systems and toolchains.

## Outline (30 minutes)

* Intro (4 minutes)
    * Problem statement
    * Applications vs libraries
    * PyPI, pip, build systems, and virtualenvs
* Foundation (6 minutes)
	* Project metadata
		* PEP517/pyproject.toml
		* PEP621 `[project]` with Flit or setuptools
	* Dependency management
		* Metadata vs requirements.txt
		* Best practices on version constraints, pinning
		* Python/OS constraints and “markers”
	* Basic testing and validation
		* Reproducible environments
		* Command runners, make/tox/nox/etc, pick one
		* Unit tests, coverage
		* Using pessimist to validate dependencies and version constraints
* Code Quality (6 minutes)
	* Formatting, import sorting with black, µsort
	* Linting with flake8 or pylint
	* Progressive type hints and type checks with mypy or pylance
	* Documentation with Sphinx autodoc, docstrings, RTD
	* Dependency updates with Dependabot or pyup.io
* Pull Requests (6 minutes)
	* Contributor guides, COC, etc
	* CI with Github Actions
	* Enforce testing, coverage, code quality, docs changes
	* PR/Issue templates
	* Saved replies, bots, and actions
	* Dealing with "bad actors"
* Releasing Code (6 minutes)
	* Versioning, be predictable
	* Automating a changelog, using attribution or similar
	* Validate tests, lint, etc
	* Publish sdist and wheels, cibuildwheel for native code
* Conclusion (2 minutes)

## Past Experience

I have previously spoken at PyCon US on the topic of AsyncIO and multiprocessing, and gave a lightning talk at the first Maintainers' Summit. I have also given multiple talks at North Bay Python, PyCascades, and PyCon Australia, on a variety of technical topics.

I am the founder of the Omnilib Project, an inclusive home for MIT-licensed packages, and actively maintain more than 15 projects on PyPI. I am currently employed at a large tech company, working on developer tooling and infrastructure, including systems for automatically importing and integrating open source packages from PyPI into our internal build systems. I have deep knowledge into packaging, PEP 517 build systems, and the nuances of the modern open source ecosystem.

## Concept
Modern tips and guidance for running open source projects with as little overhead as possible.

* PEP517 pyproject.toml metadata, and packaging with Flit
* Requirements files and dependency constraints
* Coverage and unit testing
* Simple linting and formatting with “flake8” and “µfmt”
* Docs via RTD
* Simple CI setup with Github Actions
* Dependabot for automatic dependency updates
* PR/Issue templates, and saved replies
* Using “attribution” for version, release notes, and changelog
* Publishing releases
