#!/usr/bin/env python3

import os

from . import tokeniser
from . import parser

def render(fname, context={}):
	with open(fname) as f:
		content = f.read()
	return _render(content, context, os.path.dirname(fname))

def _render(content, context={}, path="."):
	return parser.Parser(tokeniser.tokenise(content)).parse().render(context, path)
