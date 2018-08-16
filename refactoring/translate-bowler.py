#!/usr/bin/env bowler
# Copyright 2018 John Reese
# Licensed under the MIT License

import re
from bowler.helpers import print_tree
from bowler.query import Query
from bowler.types import TOKEN
from fissix.fixer_util import Call, Name

todo_re = re.compile(r"# todo: i18n.*\n\s*", flags=re.I)


def takes_string(ln, cap, fn):
    args = cap.get('function_arguments')
    return args[0].type == TOKEN.STRING


def translate_string(ln, cap, fn):
    # wrap string in a call to tr()
    args = cap.get('function_arguments')
    args[0].replace(
        Call(
            Name("tr"),
            args=[args[0].clone()]
        ),
    )

    # drop a leading comment
    while not ln.prefix:
        prev = ln.prev_sibling
        if prev is None and ln.parent is None:
            break
        ln = prev or ln.parent
    ln.prefix = todo_re.sub("", ln.prefix)


(
    Query("source.py")
    .select_function("print")
    .is_call()
    .filter(takes_string)
    .modify(translate_string)
    .diff()
)
