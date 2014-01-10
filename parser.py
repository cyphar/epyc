#!/usr/bin/env python3

import render

class Parser:
  "Main parsing class."
  def __init__(self, tokens):
    self.tokens = tokens
    self.pos = 0
    self.length = len(tokens)

  def end(self):
    return self.pos == self.length

  def peek(self):
    if not self.end():
      return self.tokens[self.pos]

  def next(self):
    if not self.end():
      self.pos += 1

  def _parse_token(self):
    if self.end():
      return None

    # expr
    if self.peek() == "{{":
      self.next()

      expr = render.ExprNode(self.peek())
      self.next()

      if not expr or self.peek() != "}}":
        raise ParseError("error parsing expression")

      return expr
    # text
    else:
      return render.TextNode(self.peek())

  def _parse_group(self):
    groups = []

    while not self.end():
      groups.append(self._parse_token())
      self.next()

    groups = [group for group in groups if group]
    return render.GroupNode(groups)

  def parse(self):
    # EBNF for epyc:
    # group = (token)+
    # token = expr
    # token = text
    # expr  = {{ <any python expression> }}
    # text  = <any text>

    return self._parse_group()
