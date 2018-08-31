#!/usr/bin/env python
# Copyright 2018 John Reese
# Licensed under the MIT License

import logging
import re

from lib2to3.fixer_base import BaseFix
from lib2to3.fixer_util import Call, Name
from lib2to3.pytree import Base, Node, Leaf, type_repr
from lib2to3.main import StdoutRefactoringTool
from lib2to3.pygram import python_symbols as symbol
from lib2to3.pgen2 import token


class I18n(BaseFix):
    """
    Wrap calls to print with string literals in tr()
    and drop any leading `# TODO: i18n` comments.

    Before:
        # TODO: i18n
        print("Hello world!")

    After:
        print(tr("Hello world!"))

    """

    PATTERN = """
        power< 'print'
            trailer< '(' s=STRING ')' >
        >
    """

    def transform(self, node, results):
        # wrap string in a call to tr()
        literal = results["s"]
        literal.replace(
            Call(
                Name("tr"),
                args=[literal.clone()]
            ),
        )

        # drop a leading comment
        node.prefix = re.sub(
            r"# TODO: i18n.*\n\s*",
            "",
            node.prefix
        )

        return node


class SimpleRefactor(StdoutRefactoringTool):
    """
    Make the refactoring tool work on a list
    of classes, instead of importing by name.
    """
    def get_fixers(self):
        fixers = [
            f(self.options, self.fixer_log)
            for f in self.fixers
        ]
        return fixers, ()

    def __init__(self, *fixers, **kwargs):
        super(SimpleRefactor, self).__init__(fixers, {"print_function": True}, [], True, True, **kwargs)


if __name__ == "__main__":
    tool = SimpleRefactor(I18n)
    tool.refactor(['source.py'])
    tool.summarize()
