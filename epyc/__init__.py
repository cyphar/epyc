#!/usr/bin/env python3

from . import tokeniser
from . import parser

def render(fname, scope={}):
    with open(fname) as f:
        content = f.read()
    return _render(content, scope)

def _render(content, scope={}):
    return parser.Parser(tokeniser.tokenise(content)).parse().render(scope)
